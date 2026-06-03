from fastapi import FastAPI, Response
import sqlite3

app = FastAPI()

def init_db():
    conn = sqlite3.connect("counter.db")
    conn.execute("CREATE TABLE IF NOT EXISTS stats (key TEXT PRIMARY KEY, count INTEGER)")
    conn.execute("INSERT OR IGNORE INTO stats VALUES ('views', 0)")
    conn.commit()
    conn.close()

init_db()

@app.get("/view")
async def get_counter():
    conn = sqlite3.connect("counter.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE stats SET count = count + 1 WHERE key = 'views'")
    cursor.execute("SELECT count FROM stats WHERE key = 'views'")
    count = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    svg_content = f"""<svg width="200" height="40" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="#0a0a0c" rx="6"/>
        <text x="10" y="25" fill="#ff6a00" font-family="monospace">views: {count}</text>
    </svg>"""

    return Response(content=svg_content, media_type="image/svg+xml", headers={"Cache-Control": "no-cache"})
