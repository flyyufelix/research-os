(function () {
  const menuButton = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("[data-site-nav]");

  if (menuButton && menu) {
    menuButton.addEventListener("click", function () {
      const open = menu.getAttribute("data-open") === "true";
      menu.setAttribute("data-open", String(!open));
      menuButton.setAttribute("aria-expanded", String(!open));
    });
  }

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", async function () {
      const block = button.closest(".code-block");
      const code = block && block.querySelector("code");
      if (!code) return;

      const original = button.textContent;
      try {
        await navigator.clipboard.writeText(code.textContent.trim());
        button.textContent = "Copied";
      } catch (error) {
        button.textContent = "Select text";
      }

      window.setTimeout(function () {
        button.textContent = original;
      }, 1800);
    });
  });
})();

