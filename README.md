**<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zligh Core Terminal</title>
    <style>
        /* --- КВАНТОВЫЙ РЕФАКТОРИНГ СТИЛЕЙ (ЧИСТЫЙ CSS) --- */
        :root {
            --bg-color: #0a0a0c;
            --terminal-bg: #0d0d11;
            --text-primary: #a370f7; /* Твой каноничный фиолетовый вайб Лайта */
            --text-success: #00ff66; /* Ядерный зеленый для логов */
            --border-brutal: 3px solid #1a1a24;
            --glow: 0 0 15px rgba(163, 112, 247, 0.4);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Courier New', Courier, monospace;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            overflow: hidden;
            position: relative;
        }

        /* --- ЭФФЕКТ СТАРOГО CRT МОНИТОРА --- */
        body::after {
            content: " ";
            display: block;
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            aspect-ratio: initial;
            background-size: 100% 3px, 6px 100%;
            pointer-events: none;
            z-index: 999;
        }

        /* --- БРУТАЛЬНЫЙ КОНТЕЙНЕР ТЕРМИНАЛА --- */
        .terminal-container {
            width: 100%;
            max-width: 850px;
            background-color: var(--terminal-bg);
            border: var(--border-brutal);
            box-shadow: var(--glow);
            position: relative;
            transform: scale(0.98);
            animation: bootUp 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        }

        /* Хедер окна в стиле Linux */
        .terminal-header {
            background-color: #12121a;
            padding: 10px;
            border-bottom: var(--border-brutal);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .window-title {
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .window-controls {
            display: flex;
            gap: 8px;
        }

        .control-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #1a1a24;
        }
        .control-dot.close { background-color: #ff5f56; }

        /* Рабочая матрица вывода данных */
        .terminal-body {
            padding: 25px;
            font-size: 15px;
            line-height: 1.6;
        }

        /* --- ПОТОКОВАЯ АНИМАЦИЯ ПОЯВЛЕНИЯ СТРОК --- */
        .log-line {
            opacity: 0;
            white-space: pre-wrap;
            margin-bottom: 8px;
        }

        .log-line.success { color: var(--text-success); }
        .log-line.cyan { color: #00ffff; }
        .log-line.white { color: #ffffff; }

        /* Тайминги жесткого каскадного раскрытия */
        .line-1 { animation: fadeInLine 0.1s 0.2s forwards; }
        .line-2 { animation: fadeInLine 0.1s 0.5s forwards; }
        .line-3 { animation: fadeInLine 0.1s 0.8s forwards; }
        .line-4 { animation: fadeInLine 0.1s 1.2s forwards; }
        .line-5 { animation: fadeInLine 0.1s 1.5s forwards; }
        .line-6 { animation: fadeInLine 0.1s 1.8s forwards; }
        .line-7 { animation: fadeInLine 0.1s 2.2s forwards; }
        .line-8 { animation: fadeInLine 0.1s 2.5s forwards; }

        .ascii-art {
            color: #ffffff;
            font-size: 12px;
            line-height: 1.2;
            margin-bottom: 20px;
            opacity: 0;
            animation: fadeInLine 0.3s 1.0s forwards;
        }

        /* Мигающий хакерский курсор CLI */
        .cursor {
            display: inline-block;
            width: 10px;
            height: 18px;
            background-color: var(--text-primary);
            animation: blink 0.8s infinite;
            vertical-align: middle;
        }

        /* --- КЛЮЧЕВЫЕ КАДРЫ АНИМАЦИЙ --- */
        @keyframes bootUp {
            0% { transform: scale(0.3) rotateX(90deg); opacity: 0; filter: brightness(3); }
            100% { transform: scale(1) rotateX(0deg); opacity: 1; filter: brightness(1); }
        }

        @keyframes fadeInLine {
            0% { opacity: 0; transform: translateX(-10px); }
            100% { opacity: 1; transform: translateX(0); }
        }

        @keyframes blink {
            0%, 49% { opacity: 1; }
            50%, 100% { opacity: 0; }
        }
    </style>
</head>
<body>

    <!-- --- СТРУКТУРА МОНОЛИТА --- -->
    <div class="terminal-container">
        <div class="terminal-header">
            <div class="window-title">root@Zligh: /dev/rawsh-core</div>
            <div class="window-controls">
                <div class="control-dot"></div>
                <div class="control-dot"></div>
                <div class="control-dot close"></div>
            </div>
        </div>
        <div class="terminal-body">
            <div class="log-line line-1 success">[INITIALIZING]: Kernel boot process started successfully.</div>
            <div class="log-line line-2 cyan">$ neofetch --backend rawsh-core</div>
            
            <!-- ASCII-Логотип Rust ядра -->
            <pre class="ascii-art">
    ######      OS: Ubuntu Linux Core (Custom Minimal Layout)
   #######     Kernel: Rust nightly v1.94.0
   ##O#O##     Shell: rawsh-core (Custom built from scratch)
   #######     CPU: native-x86 (Optimized thread pool)
   #######     RAM: Max efficiency / Zero Throttling
    #####      Benchmark: 1,000,000,000 ops in 55ms
            </pre>

            <div class="log-line line-3 cyan">$ cat active_architecture.log</div>
            <div class="log-line line-4 white">> ados-engine :: Private asynchronous 3D Game Engine (0.5MB binary).</div>
            <div class="log-line line-5 white">> mulados-lang:: Custom compiler/interpreter for internal .ms scripts.</div>
            <div class="log-line line-6 white">> data-pipeline:: Deep source agnosticism (independent IO streams).</div>
            
            <div class="log-line line-7 success">[SUCCESS]: Split Editor Pipeline loaded (Render Window + egui Layout).</div>
            <div class="log-line line-8 cyan">Zligh@ados-engine:~$ <span class="cursor"></span></div>
        </div>
    </div>

</body>
</html>
**
