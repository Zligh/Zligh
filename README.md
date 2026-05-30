![Zligh Core](./core.svg)

<div align="center">

<div class="terminal-container">
  <div class="terminal-header">
    <span class="terminal-title">zligh@rust:~$</span>
  </div>
  <div class="terminal-content">
    <div class="water-animation"></div>
    <div class="terminal-text">Just Use Rust. Brutal</div>
  </div>
</div>

<style>
.terminal-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 40px auto;
  background: rgba(10, 10, 15, 0.7);
  border: 2px solid rgba(255, 107, 0, 0.3);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  box-shadow: 0 0 30px rgba(255, 107, 0, 0.1), inset 0 0 30px rgba(255, 107, 0, 0.05);
  overflow: hidden;
  animation: glassglow 3s ease-in-out infinite;
}

@keyframes glassglow {
  0%, 100% {
    border-color: rgba(255, 107, 0, 0.3);
    box-shadow: 0 0 30px rgba(255, 107, 0, 0.1), inset 0 0 30px rgba(255, 107, 0, 0.05);
  }
  50% {
    border-color: rgba(255, 107, 0, 0.6);
    box-shadow: 0 0 50px rgba(255, 107, 0, 0.2), inset 0 0 40px rgba(255, 107, 0, 0.1);
  }
}

.terminal-header {
  background: rgba(0, 0, 0, 0.5);
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255, 107, 0, 0.2);
  backdrop-filter: blur(10px);
}

.terminal-title {
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  color: #ff6b00;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1px;
}

.terminal-content {
  position: relative;
  padding: 60px 40px;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: linear-gradient(135deg, rgba(15, 15, 20, 0.8), rgba(20, 10, 5, 0.8));
}

.water-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 20% 50%, rgba(255, 107, 0, 0.1) 0%, transparent 50%), radial-gradient(circle at 80% 50%, rgba(255, 107, 0, 0.05) 0%, transparent 50%), repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(255, 107, 0, 0.05) 2px, rgba(255, 107, 0, 0.05) 4px);
  animation: waterflow 4s ease-in-out infinite;
  pointer-events: none;
}

@keyframes waterflow {
  0%, 100% {
    background-position: 0 0;
    opacity: 0.3;
  }
  50% {
    opacity: 0.6;
  }
}

.terminal-text {
  position: relative;
  z-index: 2;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 28px;
  font-weight: bold;
  color: #ff6b00;
  text-shadow: 0 0 10px rgba(255, 107, 0, 0.8), 0 0 20px rgba(255, 107, 0, 0.4);
  letter-spacing: 2px;
  animation: typewriter 0.5s steps(24, end), glow 2.5s ease-in-out infinite 0.5s;
  white-space: nowrap;
}

@keyframes typewriter {
  from {
    width: 0;
  }
  to {
    width: 24ch;
  }
}

@keyframes glow {
  0%, 100% {
    text-shadow: 0 0 10px rgba(255, 107, 0, 0.8), 0 0 20px rgba(255, 107, 0, 0.4);
  }
  50% {
    text-shadow: 0 0 20px rgba(255, 107, 0, 1), 0 0 40px rgba(255, 107, 0, 0.6), 0 0 60px rgba(255, 107, 0, 0.3);
  }
}
</style>

</div>