const upInforme = () => {
  const identificador = document.getElementById("murl").innerHTML;
  const texto = document.getElementById("ventas").value;
  const mensaje = document.getElementById("respuesta");
  const dato = [identificador, texto];
  const arrayJson = JSON.stringify(dato);

  fetch("updateInforme.php", { method: "POST", body: arrayJson })
    .then((res) => res.json())
    .then((respuesta) => {
      if (respuesta === "error") {
        window.alert("Informe de Ventas Actualizado Exitosamente.");
        window.location.href = window.location.href;
        // window.location.reload();
      } else {
        if (respuesta === "error4") {
          window.alert("No se pudo actualizar los informes de Ventas.");
          window.location.href = window.location.href;
        }
      }
    });
};

document.getElementById("area2").addEventListener("change", function (e) {
  const mensaje = document.getElementById("respuesta");
  const aa = this.value;
  var area = aa.split("|");
  const id_area = area[0];
  const str_area = area[1];
  mensaje.textContent = "";
  if (this.value != "") {
    document.getElementById("ventas").value = str_area;
    document.getElementById("murl").innerHTML = id_area;
  }
  if (mensaje.classList.contains("alert-danger")) {
    mensaje.classList.remove("alert-danger");
  }
  if (mensaje.classList.contains("alert-success")) {
    mensaje.classList.remove("alert-success");
  }
});
