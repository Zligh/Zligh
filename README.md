![Zligh Core](./core.svg)

<div align="center">

```svg
<svg viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="terminalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f0f14;stop-opacity:0.8" />
      <stop offset="100%" style="stop-color:#140a05;stop-opacity:0.8" />
    </linearGradient>
    <style>
      @keyframes glow { 
        0%, 100% { filter: drop-shadow(0 0 5px #ff6b00); }
        50% { filter: drop-shadow(0 0 15px #ff6b00); }
      }
      @keyframes float {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.7; }
      }
      .terminal { animation: glow 2s ease-in-out infinite; }
      .water { animation: float 3s ease-in-out infinite; }
      .text { animation: glow 2.5s ease-in-out infinite; }
    </style>
  </defs>
  
  <!-- Terminal Window -->
  <rect class="terminal" x="20" y="20" width="560" height="210" rx="12" fill="url(#terminalGrad)" stroke="#ff6b00" stroke-width="2" opacity="0.9"/>
  
  <!-- Header -->
  <rect x="20" y="20" width="560" height="35" rx="12" fill="rgba(0,0,0,0.5)" stroke="#ff6b00" stroke-width="2" stroke-opacity="0.3"/>
  <text x="35" y="47" font-family="Monaco, monospace" font-size="13" fill="#ff6b00" font-weight="600">zligh@rust:~$</text>
  
  <!-- Water effect background -->
  <circle class="water" cx="100" cy="120" r="60" fill="#ff6b00" opacity="0.08"/>
  <circle class="water" cx="500" cy="100" r="80" fill="#ff6b00" opacity="0.05"/>
  <circle class="water" cx="300" cy="180" r="50" fill="#ff6b00" opacity="0.06"/>
  
  <!-- Main text -->
  <text class="text" x="300" y="135" font-family="Monaco, monospace" font-size="32" font-weight="bold" fill="#ff6b00" text-anchor="middle" filter="url(#glow)">Just Use Rust. Brutal</text>
</svg>
```

</div>