n = 900;
var id = window.setInterval(() => {
  document.onmousemove = function () {
    n = 900;
  };
  n--;
  if (n <= -1) {
    window.location.href = "cerrarSesion.php";
  }
}, 1200);
