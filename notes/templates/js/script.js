$(document).ready(function() {
    // Listen for click event on the paragraph
    $("#termsLink").click(function() {
        // Show the modal
        $("#exampleModal").modal("show");
    });
});

function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }

  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  // For Demo Purpose [Changing input group text on focus]
  $(function () {
    $('input, select').on('focus', function () {
      $(this).parent().find('.input-group-text').css('border-color', '#80bdff');
    });
    $('input, select').on('blur', function () {
      $(this).parent().find('.input-group-text').css('border-color', '#ced4da');
    });
  });

// dark mode toggle
function toggleTheme() {
  var htmlElement = document.documentElement;
  var themeToggleBtn = document.getElementById('themeToggleBtn');
  var currentTheme = htmlElement.getAttribute('data-bs-theme');
  var navbar = document.getElementById('navbar'); // Get the navbar element
  var openbtn = document.querySelector('.openbtn'); // Get the openbtn element

  if (currentTheme === 'dark') {
      htmlElement.setAttribute('data-bs-theme', 'light');
      themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
      localStorage.setItem('theme', 'light');
      navbar.classList.remove('navbar-dark'); // Remove navbar-dark class
      navbar.classList.remove('bg-dark'); // Remove bg-dark class
      navbar.classList.add('navbar-light'); // Add navbar-light class
      navbar.classList.add('bg-light'); // Add bg-light class

      
      openbtn.classList.add('openbtn-custom-style');

  } else {
      htmlElement.setAttribute('data-bs-theme', 'dark');
      themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
      localStorage.setItem('theme', 'dark');
      navbar.classList.remove('navbar-light'); // Remove navbar-light class
      navbar.classList.remove('bg-light'); // Remove bg-light class
      navbar.classList.add('navbar-dark'); // Add navbar-dark class
      navbar.classList.add('bg-dark'); // Add bg-dark class

  }
}

// Function to set the theme based on localStorage when the page loads
window.onload = function() {
  var theme = localStorage.getItem('theme');
  if (theme) {
      document.documentElement.setAttribute('data-bs-theme', theme);
      if (theme === 'light') {
          document.getElementById('themeToggleBtn').innerHTML = '<i class="fas fa-sun"></i>';
      } else {
          document.getElementById('themeToggleBtn').innerHTML = '<i class="fas fa-moon"></i>';
          document.getElementById('navbar').classList.remove('navbar-light'); // Remove navbar-light class
          document.getElementById('navbar').classList.remove('bg-light'); // Remove bg-light class
          document.getElementById('navbar').classList.add('navbar-dark'); // Add navbar-dark class
          document.getElementById('navbar').classList.add('bg-dark'); // Add bg-dark class

      }
  }
}
