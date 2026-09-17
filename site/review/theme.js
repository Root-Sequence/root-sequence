(function () {
  'use strict';
  var root = document.documentElement;
  var key = 'site-theme-v1-' + (root.getAttribute('data-site') || 'default');
  var allowed = ['system', 'light', 'dark'];
  var current = 'system';
  try { var saved = localStorage.getItem(key); if (allowed.indexOf(saved) >= 0) current = saved; } catch (_) {}
  function apply(value) {
    current = allowed.indexOf(value) >= 0 ? value : 'system';
    if (current === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', current);
    document.querySelectorAll('input[name="color-theme"]').forEach(function (input) { input.checked = input.value === current; });
  }
  apply(current);
  function init() {
    var controls = document.getElementById('theme-controls');
    if (!controls) return;
    controls.hidden = false;
    apply(current);
    controls.addEventListener('change', function (event) {
      if (event.target.name !== 'color-theme') return;
      apply(event.target.value);
      try { if (current === 'system') localStorage.removeItem(key); else localStorage.setItem(key, current); } catch (_) {}
    });
    window.addEventListener('storage', function (event) {
      if (event.key === key || event.key === null) apply(allowed.indexOf(event.newValue) >= 0 ? event.newValue : 'system');
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
}());
