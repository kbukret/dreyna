const calculaPantalla = () => {
  const pantalla = document.getElementById("logocentral");
  let cuanto = 0;

  console.log(screen.height);
  if (screen.height < 641) {
    cuanto = Math.trunc(screen.height / 3);
  } else {
    if (screen.height < 769) {
      cuanto = Math.trunc(screen.height / 2.4);
    } else {
      cuanto = Math.trunc(screen.height / 2);
    }
  }
  console.log(cuanto.toString() + "px");
  pantalla.style.marginTop = cuanto.toString() + "px";
};
calculaPantalla();
