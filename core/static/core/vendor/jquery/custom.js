document.addEventListener('DOMContentLoaded', function () {
  console.log('custom.js cargado correctamente ✅');

  const dropdownToggle = document.getElementById('formacionDropdown');
  const dropdownMenu = dropdownToggle ? dropdownToggle.nextElementSibling : null;

  if (dropdownToggle && dropdownMenu) {
    console.log('Dropdown detectado');

    dropdownToggle.addEventListener('click', function (e) {
      e.preventDefault();
      dropdownMenu.classList.toggle('show');
      console.log('Dropdown clicado, clase "show" alternada');
    });

    document.addEventListener('click', function (e) {
      if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.classList.remove('show');
        console.log('Clic fuera del dropdown, clase "show" eliminada');
      }
    });
  } else {
    console.warn('⚠️ Dropdown no encontrado en el DOM');
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const proyectos = document.querySelectorAll('.row.project');

  if (proyectos.length > 0) {
    console.log(`Se encontraron ${proyectos.length} elementos .row.project`);

    proyectos.forEach(function (div) {
      div.addEventListener('mouseover', function () {
        div.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
        div.style.borderRadius = '10px';
        console.log('Mouseover en proyecto');
      });

      div.addEventListener('mouseout', function () {
        div.style.backgroundColor = '';
        div.style.borderRadius = '';
        console.log('Mouseout en proyecto');
      });
    });
  } else {
    console.warn('⚠️ No se encontraron elementos .row.project');
  }
});