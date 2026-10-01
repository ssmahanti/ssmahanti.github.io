$(function () {
  // Shared navigation and footer for every page.
  $("#navbar-include").load("navbar.html", function (_, status) {
    if (status === "error") {
      $(this).html('<p class="container"><a href="index.html">Home</a> · <a href="projects.html">Projects</a> · <a href="publication.html">Publications</a> · <a href="outreach.html">Outreach</a> · <a href="vitae.html">CV</a></p>');
      return;
    }
    const page = location.pathname.split("/").pop() || "index.html";
    $(this).find(".navbar-nav a").each(function () {
      if ($(this).attr("href") === page) {
        $(this).attr("aria-current", "page").parent().addClass("active");
      }
    });
  });
  $("#page-footer").load("footer.html", function (_, status) {
    if (status === "error") {
      $(this).text("Sankha Subhra Mahanti · smahanti@ucsd.edu");
      return;
    }
    $("#footer-year").text(new Date().getFullYear());
  });

  const topper = document.getElementById("topper");
  if (topper) {
    const updateTopper = function () {
      topper.style.display = window.scrollY > 80 ? "block" : "none";
    };
    window.addEventListener("scroll", updateTopper, { passive: true });
    updateTopper();
  }
});
