/* Healthify AI · body map
   A point-cloud body built from simple shapes, drawn on a 2D canvas.
   Pain spots glow in the attention colour and vibrate; rings travel over the skin.
   HFBody(canvas, {theme, points, seed}) -> {setSpots, focus, view, setTime, frame, area, destroy} */
(function (root) {
  'use strict';
  function rng(seed) { var s = seed >>> 0 || 1; return function () { s ^= s << 13; s >>>= 0; s ^= s >> 17; s ^= s << 5; s >>>= 0; return s / 4294967296; }; }
  function len(x, y, z) { return Math.sqrt(x * x + y * y + z * z); }

  // ---- body parts (metres, y up, +z faces the viewer, +x is the viewer's right)
  function parts() {
    var P = [];
    function E(c, r) { P.push({ t: 'e', c: c, r: r }); }
    function C(a, b, r1, r2) { P.push({ t: 'c', a: a, b: b, r1: r1, r2: r2 }); }
    E([0, 1.625, 0.005], [0.088, 0.118, 0.105]);            // head
    C([0, 1.455, -0.005], [0, 1.545, 0], 0.052, 0.048);     // neck
    P.push({ t: 'l', p: 2.6, L: [ // torso: y, half-width, half-depth, z-centre
      [0.845, 0.115, 0.075, -0.005], [0.880, 0.165, 0.098, -0.008], [0.930, 0.178, 0.106, -0.008], [1.000, 0.162, 0.100, -0.002],
      [1.090, 0.145, 0.094, 0.004], [1.190, 0.158, 0.098, 0.006], [1.290, 0.180, 0.108, 0.006], [1.370, 0.192, 0.102, 0.0],
      [1.425, 0.165, 0.085, -0.008], [1.465, 0.080, 0.058, -0.008]] });
    [-1, 1].forEach(function (s) {
      E([s * 0.185, 1.395, -0.005], [0.062, 0.055, 0.058]); // shoulder
      C([s * 0.205, 1.395, 0], [s * 0.265, 1.120, 0.005], 0.050, 0.041);   // upper arm
      C([s * 0.265, 1.120, 0.005], [s * 0.305, 0.870, 0.030], 0.039, 0.029); // forearm
      E([s * 0.315, 0.795, 0.035], [0.026, 0.060, 0.022]);  // hand
      C([s * 0.090, 0.900, 0], [s * 0.100, 0.505, 0.005], 0.078, 0.054);  // thigh
      C([s * 0.100, 0.505, 0.005], [s * 0.106, 0.095, -0.012], 0.051, 0.034); // shin
      E([s * 0.106, 0.040, 0.045], [0.040, 0.034, 0.095]);  // foot
    });
    return P;
  }
  function loftAt(q, y) { var L = q.L; if (y <= L[0][0]) return L[0]; if (y >= L[L.length - 1][0]) return L[L.length - 1];
    for (var i = 0; i < L.length - 1; i++) if (y <= L[i + 1][0]) { var a = L[i], b = L[i + 1], t = (y - a[0]) / (b[0] - a[0]); t = t * t * (3 - 2 * t); return [y, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t, a[3] + (b[3] - a[3]) * t]; } }
  function inside(p, q, pad) {
    if (q.t === 'l') { var L = q.L; if (p[1] < L[0][0] || p[1] > L[L.length - 1][0]) return false; var c = loftAt(q, p[1]); return Math.pow(Math.abs(p[0] / (c[1] - pad)), q.p) + Math.pow(Math.abs((p[2] - c[3]) / (c[2] - pad)), q.p) < 1; }
    if (q.t === 'e') { var dx = (p[0] - q.c[0]) / (q.r[0] - pad), dy = (p[1] - q.c[1]) / (q.r[1] - pad), dz = (p[2] - q.c[2]) / (q.r[2] - pad); return dx * dx + dy * dy + dz * dz < 1; }
    var ax = q.b[0] - q.a[0], ay = q.b[1] - q.a[1], az = q.b[2] - q.a[2], L2 = ax * ax + ay * ay + az * az;
    var t = ((p[0] - q.a[0]) * ax + (p[1] - q.a[1]) * ay + (p[2] - q.a[2]) * az) / L2; t = Math.max(0, Math.min(1, t));
    var cx = q.a[0] + ax * t, cy = q.a[1] + ay * t, cz = q.a[2] + az * t, r = q.r1 + (q.r2 - q.r1) * t - pad;
    return len(p[0] - cx, p[1] - cy, p[2] - cz) < r;
  }
  function sample(n, seed) {
    var R = rng(seed), P = parts(), area = P.map(function (q) {
      if (q.t === 'l') { var A = 0; for (var i = 0; i < q.L.length - 1; i++) { var u = q.L[i], w = q.L[i + 1]; A += Math.PI * (u[1] + u[2] + w[1] + w[2]) / 2 * (w[0] - u[0]); } return A; }
      if (q.t === 'e') { var a = q.r[0], b = q.r[1], c = q.r[2], p = 1.6; return 4 * Math.PI * Math.pow((Math.pow(a * b, p) + Math.pow(a * c, p) + Math.pow(b * c, p)) / 3, 1 / p); }
      var L = len(q.b[0] - q.a[0], q.b[1] - q.a[1], q.b[2] - q.a[2]); return 2 * Math.PI * (q.r1 + q.r2) / 2 * L + 2 * Math.PI * (q.r1 * q.r1 + q.r2 * q.r2);
    }), tot = area.reduce(function (s, a) { return s + a; }, 0), out = [];
    P.forEach(function (q, qi) {
      var k = Math.round(n * area[qi] / tot * 1.25), made = 0, guard = 0;
      while (made < k && guard++ < k * 6) {
        var p, nr;
        if (q.t === 'l') {
          var y0 = q.L[0][0], y1 = q.L[q.L.length - 1][0], yy = y0 + R() * (y1 - y0), c = loftAt(q, yy), an = R() * Math.PI * 2, ca2 = Math.cos(an), sa2 = Math.sin(an);
          var e = 2 / q.p, cx2 = Math.sign(ca2) * Math.pow(Math.abs(ca2), e), sz2 = Math.sign(sa2) * Math.pow(Math.abs(sa2), e);
          p = [c[1] * cx2, yy, c[3] + c[2] * sz2];
          var c2 = loftAt(q, yy + .01), dr = ((c2[1] - c[1]) * Math.abs(cx2) + (c2[2] - c[2]) * Math.abs(sz2)) / .01;
          nr = [Math.sign(ca2) * Math.pow(Math.abs(ca2), 2 - e) / c[1], -dr * 0.9, Math.sign(sa2) * Math.pow(Math.abs(sa2), 2 - e) / c[2]];
          var top = yy > y1 - .03 ? 1 : 0; if (top) nr[1] += 6;
        } else if (q.t === 'e') {
          var u = R() * 2 - 1, th = R() * Math.PI * 2, s = Math.sqrt(1 - u * u), d = [s * Math.cos(th), u, s * Math.sin(th)];
          p = [q.c[0] + d[0] * q.r[0], q.c[1] + d[1] * q.r[1], q.c[2] + d[2] * q.r[2]];
          nr = [d[0] / q.r[0], d[1] / q.r[1], d[2] / q.r[2]];
        } else {
          var ax = q.b[0] - q.a[0], ay = q.b[1] - q.a[1], az = q.b[2] - q.a[2], L = len(ax, ay, az); ax /= L; ay /= L; az /= L;
          var ux = 1, uy = 0, uz = 0; if (Math.abs(ax) > .9) { ux = 0; uy = 0; uz = 1; }
          var vx = ay * uz - az * uy, vy = az * ux - ax * uz, vz = ax * uy - ay * ux, vl = len(vx, vy, vz); vx /= vl; vy /= vl; vz /= vl;
          ux = vy * az - vz * ay; uy = vz * ax - vx * az; uz = vx * ay - vy * ax;
          var t = R(), a = R() * Math.PI * 2, r = q.r1 + (q.r2 - q.r1) * t, ca = Math.cos(a), sa = Math.sin(a);
          nr = [ux * ca + vx * sa, uy * ca + vy * sa, uz * ca + vz * sa];
          p = [q.a[0] + ax * L * t + nr[0] * r, q.a[1] + ay * L * t + nr[1] * r, q.a[2] + az * L * t + nr[2] * r];
        }
        var nl = len(nr[0], nr[1], nr[2]); nr = [nr[0] / nl, nr[1] / nl, nr[2] / nl];
        var hidden = false; for (var j = 0; j < P.length && !hidden; j++) if (j !== qi && inside(p, P[j], 0.004)) hidden = true;
        if (hidden) continue;
        out.push({ p: p, n: nr, r: R(), ph: R() * Math.PI * 2 }); made++;
      }
    });
    return out;
  }

  // ---- named areas: where they are and which side to look from
  var AREAS = {
    head:      { name: 'Head',        pos: [0.055, 1.665, 0.080], yaw: 0.35 },
    neck:      { name: 'Neck',        pos: [0.000, 1.490, -0.050], yaw: Math.PI },
    shoulder:  { name: 'Left shoulder', pos: [0.200, 1.440, 0.010], yaw: 0.45 },
    chest:     { name: 'Chest',       pos: [-0.060, 1.330, 0.100], yaw: -0.15 },
    stomach:   { name: 'Stomach',     pos: [0.030, 1.070, 0.100], yaw: 0.1 },
    lowerback: { name: 'Lower back',  pos: [0.040, 1.030, -0.092], yaw: Math.PI - 0.25 },
    knee:      { name: 'Right knee',  pos: [-0.100, 0.505, 0.052], yaw: -0.2 },
    wrist:     { name: 'Right wrist', pos: [-0.300, 0.870, 0.030], yaw: -0.4 }
  };

  var THEMES = {
    dark:  { dot: [242, 242, 238], hot: [255, 91, 46], bg: null },
    paper: { dot: [15, 15, 18], hot: [255, 91, 46], bg: null }
  };

  function HFBody(canvas, o) {
    o = o || {};
    var ctx = canvas.getContext('2d'), pts = sample(o.points || 12000, o.seed || 7), th = THEMES[o.theme || 'dark'];
    var spots = [], time = 0, raf = 0, running = false, last = 0, fixedTime = null;
    var cam = { yaw: o.yaw || 0, pitch: o.pitch == null ? -0.06 : o.pitch, y: 0.92, dist: 3.1, fov: 1.0 }, target = null;
    var drag = null, autoSpin = o.spin || 0;
    var SX = new Float32Array(pts.length), SY = new Float32Array(pts.length), FF = new Float32Array(pts.length);

    // snap a position to the closest skin point
    function snap(pos) { var b = null, bd = 1e9; pts.forEach(function (q) { var d = len(q.p[0] - pos[0], q.p[1] - pos[1], q.p[2] - pos[2]); if (d < bd) { bd = d; b = q; } }); return b; }

    function setSpots(list) {
      spots = list.map(function (s) {
        var a = AREAS[s.area] || {}, base = snap(s.pos || a.pos);
        return { area: s.area, name: s.name || a.name, c: base.p, n: base.n, k: s.intensity == null ? .6 : s.intensity, R: s.radius || 0.075 + 0.05 * (s.intensity || .6), label: s.label, quiet: !!s.quiet, yaw: a.yaw };
      });
    }
    function view(v, instant) { // {yaw, y, dist, pitch}
      target = { yaw: v.yaw == null ? cam.yaw : v.yaw, y: v.y == null ? cam.y : v.y, dist: v.dist == null ? cam.dist : v.dist, pitch: v.pitch == null ? cam.pitch : v.pitch };
      if (instant) { cam.yaw = target.yaw; cam.y = target.y; cam.dist = target.dist; cam.pitch = target.pitch; target = null; }
    }
    function focus(area, instant, zoom) {
      var a = AREAS[area]; if (!a) return;
      var yaw = a.yaw; // shortest turn
      while (yaw - cam.yaw > Math.PI) yaw -= 2 * Math.PI; while (yaw - cam.yaw < -Math.PI) yaw += 2 * Math.PI;
      view({ yaw: yaw, y: a.pos[1] * .55 + .92 * .45, dist: zoom || 1.9 }, instant);
    }

    function frame(dt) {
      var W = canvas.width, H = canvas.height, dpr = o.dpr || (root.devicePixelRatio || 1);
      if (target) { var e = 1 - Math.pow(.002, dt); ['yaw', 'y', 'dist', 'pitch'].forEach(function (k) { cam[k] += (target[k] - cam[k]) * e; });
        if (Math.abs(target.yaw - cam.yaw) < 1e-3 && Math.abs(target.dist - cam.dist) < 1e-3) target = null; }
      else if (autoSpin && !drag) cam.yaw += autoSpin * dt;
      ctx.clearRect(0, 0, W, H);
      var cy = Math.cos(cam.yaw), sy = Math.sin(cam.yaw), cp = Math.cos(cam.pitch), sp = Math.sin(cam.pitch);
      var f = Math.min(H * 1.38, W * 2.3) * (o.scale || 1);
      var L = [-.35, .55, .76], ll = len(L[0], L[1], L[2]); L = [L[0] / ll, L[1] / ll, L[2] / ll];
      var t = time, sz = Math.max(.9, (o.dot || 1.1) * dpr);
      // spot glow behind the body
      var proj = [];
      spots.forEach(function (s) {
        var x = s.c[0], y = s.c[1] - cam.y, z = s.c[2];
        var X = x * cy + z * sy, Z = -x * sy + z * cy, Y = y * cp - Z * sp; Z = y * sp + Z * cp;
        var d = cam.dist - Z, sx = W / 2 + X * f / d, syy = H / 2 - Y * f / d;
        var nz = -s.n[0] * sy + s.n[2] * cy; // facing the camera?
        proj.push({ x: sx, y: syy, d: d, front: nz > -0.2, s: s });
        if (s.quiet) return;
        var g = ctx.createRadialGradient(sx, syy, 0, sx, syy, s.R * f / d * 1.7), a = (nz > -0.2 ? .30 : .12) * (0.7 + 0.3 * Math.sin(t * 6));
        g.addColorStop(0, 'rgba(' + th.hot + ',' + a + ')'); g.addColorStop(1, 'rgba(' + th.hot + ',0)');
        ctx.fillStyle = g; ctx.fillRect(sx - 400, syy - 400, 800, 800);
      });
      // points, painted back to front in two passes is enough for dots
      for (var i = 0; i < pts.length; i++) {
        var q = pts[i], px = q.p[0], py = q.p[1], pz = q.p[2], hot = 0, wave = 0;
        for (var j = 0; j < spots.length; j++) {
          var s = spots[j], dd = len(px - s.c[0], py - s.c[1], pz - s.c[2]);
          if (dd < s.R * 2.4) {
            var fall = Math.max(0, 1 - dd / s.R); fall = fall * fall * (3 - 2 * fall);
            var k = s.quiet ? .55 : 1;
            // vibration: fast along the normal, a little jitter sideways
            var amp = (s.quiet ? 0 : .006 + .012 * s.k) * fall, w = 38 + 30 * s.k;
            var v = amp * (Math.sin(t * w + q.ph) * .7 + Math.sin(t * w * 1.7 + q.ph * 3) * .3);
            px += q.n[0] * v + (q.r - .5) * amp * .5 * Math.sin(t * w * .9 + q.ph); py += q.n[1] * v; pz += q.n[2] * v;
            // travelling ring over the skin
            if (!s.quiet) { var ph = (t * (0.9 + s.k) + j * .37) % 1, rr = ph * s.R * 2.4, band = Math.max(0, 1 - Math.abs(dd - rr) / .012) * (1 - ph); wave = Math.max(wave, band); }
            hot = Math.max(hot, fall * k);
          }
        }
        var x = px, y = py - cam.y, z = pz;
        var X = x * cy + z * sy, Z = -x * sy + z * cy, Y = y * cp - Z * sp; Z = y * sp + Z * cp;
        FF[i] = -1; var d = cam.dist - Z; if (d < .2) continue;
        var sx = W / 2 + X * f / d, syy = H / 2 - Y * f / d;
        if (sx < -4 || syy < -4 || sx > W + 4 || syy > H + 4) continue;
        var nx = q.n[0] * cy + q.n[2] * sy, nz = -q.n[0] * sy + q.n[2] * cy, ny = q.n[1];
        SX[i] = sx; SY[i] = syy; FF[i] = nz;
        var facing = nz, lit = Math.max(0, nx * L[0] + ny * L[1] + nz * L[2]);
        var a = facing > 0 ? (.2 + .75 * lit) * (.72 + .28 * facing) : .04 + .035 * lit;
        a *= (o.alpha || 1) * (2.6 / d > 1.4 ? 1 : .8 + .2 * (2.6 / d));
        var col = th.dot;
        if (hot > 0 || wave > 0) {
          var m = Math.min(1, hot + wave * .8); col = [Math.round(col[0] + (th.hot[0] - col[0]) * m), Math.round(col[1] + (th.hot[1] - col[1]) * m), Math.round(col[2] + (th.hot[2] - col[2]) * m)];
          a = Math.min(1, a + m * (facing > 0 ? .75 : .35));
        }
        ctx.fillStyle = 'rgba(' + col[0] + ',' + col[1] + ',' + col[2] + ',' + a.toFixed(3) + ')';
        var ps = sz * (hot > .3 ? 1.25 : 1) * Math.min(1.6, 2.2 / d);
        ctx.fillRect(sx - ps / 2, syy - ps / 2, ps, ps);
      }
      // screen rings around visible, active spots
      proj.forEach(function (p) {
        if (!p.front) return;
        if (p.s.quiet) { ctx.beginPath(); ctx.arc(p.x, p.y, 2.6 * dpr, 0, Math.PI * 2); ctx.fillStyle = 'rgb(' + th.hot + ')'; ctx.fill(); return; }
        for (var r = 0; r < 3; r++) {
          var ph = (t * .8 + r / 3) % 1, rad = Math.min(60 * dpr, p.s.R * f / p.d) * (0.35 + ph * 1.15);
          ctx.beginPath(); ctx.arc(p.x, p.y, rad, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(' + th.hot + ',' + (0.55 * (1 - ph) * (0.6 + 0.4 * p.s.k)).toFixed(3) + ')'; ctx.lineWidth = 1.2 * dpr; ctx.stroke();
        }
        ctx.beginPath(); ctx.arc(p.x, p.y, 3.2 * dpr, 0, Math.PI * 2); ctx.fillStyle = 'rgb(' + th.hot + ')'; ctx.fill();
        ctx.beginPath(); ctx.arc(p.x, p.y, 7 * dpr, 0, Math.PI * 2); ctx.strokeStyle = 'rgba(' + th.hot + ',.9)'; ctx.lineWidth = 1.4 * dpr; ctx.stroke();
      });
      return proj;
    }
    function loop(ts) { if (!running) return; var dt = last ? Math.min(.05, (ts - last) / 1000) : .016; last = ts; time += dt; var pr = frame(dt); if (o.onFrame) o.onFrame(pr); raf = requestAnimationFrame(loop); }
    function start() { if (running) return; running = true; last = 0; raf = requestAnimationFrame(loop); }
    function stop() { running = false; cancelAnimationFrame(raf); }
    // nearest visible skin point to a canvas pixel
    function pick(x, y, maxd) { var b = -1, bd = (maxd || 26) * (maxd || 26); for (var i = 0; i < pts.length; i++) { if (FF[i] < .15) continue; var dx = SX[i] - x, dy = SY[i] - y, d = dx * dx + dy * dy; if (d < bd) { bd = d; b = i; } } return b < 0 ? null : pts[b].p.slice(); }
    // drag to turn, tap to mark
    if (o.interactive) {
      canvas.addEventListener('pointerdown', function (e) { drag = { x: e.clientX, y: e.clientY, yaw: cam.yaw, moved: false }; target = null; canvas.setPointerCapture(e.pointerId); });
      canvas.addEventListener('pointermove', function (e) { if (!drag) return; if (Math.abs(e.clientX - drag.x) > 4) drag.moved = true; if (drag.moved) cam.yaw = drag.yaw + (e.clientX - drag.x) * .01; });
      canvas.addEventListener('pointerup', function (e) { if (drag && !drag.moved && o.onTap) { var r = canvas.getBoundingClientRect(), k = canvas.width / r.width; var pos = pick((e.clientX - r.left) * k, (e.clientY - r.top) * k, 30 * k); if (pos) o.onTap(pos); } drag = null; });
      canvas.addEventListener('pointercancel', function () { drag = null; });
    }
    return { setSpots: setSpots, focus: focus, view: view, pick: pick, start: start, stop: stop, frame: function (dt) { return frame(dt || 0); }, setTime: function (t) { time = t; }, cam: cam, areas: AREAS };
  }
  HFBody.AREAS = AREAS;
  root.HFBody = HFBody;
})(typeof window !== "undefined" ? window : globalThis);
