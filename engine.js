// Mug Math engine: the boxes a mug order takes, the weeks a stock lasts, the cost a mug, and the minutes the printing takes. Exact integers, half-up on display only. No named constants; every number is the owner's own entry.
function _i(t, err, digits, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  if (!new RegExp("^[0-9]{1," + digits + "}$").test(t)) throw new Error(err);
  var v = parseInt(t, 10);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _p(t, err, intDigits, places, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  var m = new RegExp("^([0-9]{1," + intDigits + "})(?:\\.([0-9]{1," + places + "}))?$").exec(t);
  if (!m) throw new Error(err);
  var v = parseInt(m[1], 10) * Math.pow(10, places) + (m[2] ? parseInt(m[2].padEnd(places, "0"), 10) : 0);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _m(v) {
  var w = Math.floor(v / 100), f = String(v % 100).padStart(2, "0");
  return w + "." + f;
}
function _pl(n, one, many) { return n + (n === 1 ? one : many); }
function _v(n, one, many) { return n === 1 ? one : many; }
var _MG = "the mugs must be from 1 to 1000000 with no decimal places";
var _MB = "the mugs a box must be from 1 to 1000 with no decimal places";
var _MW = "the mugs a week must be from 1 to 100000 with no decimal places";
var _BX = "the boxes must be from 1 to 100000 with no decimal places";
var _PR = "the box price must be from 0.01 to 999.99 with up to 2 decimal places";
var _MM = "the mugs a minute must be from 1 to 100 with no decimal places";

function boxesTruth(mugs, perBox) {
  var n = _i(mugs, _MG, 7, 1, 1000000), b = _i(perBox, _MB, 4, 1, 1000);
  var k = Math.floor((n + b - 1) / b), last = n - (k - 1) * b;
  return "The " + _pl(n, " mug", " mugs") + " at " + _pl(b, " mug", " mugs") + " a box " + _v(n, "takes", "take") + " " + _pl(k, " box", " boxes") + ", the last box holding " + _pl(last, " mug", " mugs") + ".";
}
function weeksTruth(mugs, weekly) {
  var n = _i(mugs, _MG, 7, 1, 1000000), w = _i(weekly, _MW, 6, 1, 100000);
  var k = Math.floor(n / w), left = n - k * w;
  return "The " + _pl(n, " mug", " mugs") + " at " + _pl(w, " mug", " mugs") + " a week " + _v(n, "lasts", "last") + " " + _pl(k, " full week", " full weeks") + " with " + _pl(left, " mug", " mugs") + " left for the next week.";
}
function costTruth(boxes, price, mugs) {
  var b = _i(boxes, _BX, 6, 1, 100000), p = _p(price, _PR, 3, 2, 1, 99999), n = _i(mugs, _MG, 7, 1, 1000000);
  var cc = b * p;
  var pm = Math.floor((2 * cc + n) / (2 * n));
  return "The " + _pl(b, " box", " boxes") + " at $" + _m(p) + " a box " + _v(b, "comes", "come") + " to $" + _m(cc) + ", $" + _m(pm) + " a mug.";
}
function timeTruth(mugs, perMinute) {
  var n = _i(mugs, _MG, 7, 1, 1000000), m = _i(perMinute, _MM, 3, 1, 100);
  var t = Math.floor((n + m - 1) / m), h = Math.floor(t / 60), r = t % 60;
  return "The " + _pl(n, " mug", " mugs") + " at " + _pl(m, " mug", " mugs") + " a minute " + _v(n, "takes", "take") + " " + _pl(t, " minute", " minutes") + ", " + _pl(h, " hour", " hours") + " " + _pl(r, " minute", " minutes") + ".";
}
