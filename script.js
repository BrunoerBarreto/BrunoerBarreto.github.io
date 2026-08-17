// Menu mobile
const menuToggle = document.querySelector(".menu-toggle");
const navMobile = document.querySelector(".nav-mobile");

if (menuToggle && navMobile) {
  menuToggle.addEventListener("click", () => {
    const aberto = navMobile.classList.toggle("aberto");
    menuToggle.setAttribute("aria-expanded", aberto ? "true" : "false");
  });

  navMobile.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => navMobile.classList.remove("aberto"));
  });
}

// Ano atual no rodapé
const anoEl = document.getElementById("ano-atual");
if (anoEl) anoEl.textContent = new Date().getFullYear();
