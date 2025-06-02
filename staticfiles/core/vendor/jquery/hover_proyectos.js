document.addEventListener('DOMContentLoaded', function () {
    console.log('hover-proyectos.js cargado correctamente ✅');
  
    const proyectos = document.querySelectorAll('.row.project');
  
    if (proyectos.length > 0) {
      console.log(`🎯 Se encontraron ${proyectos.length} elementos .row.project`);
  
      proyectos.forEach(function (div) {
        div.addEventListener('mouseover', function () {
          div.classList.add('hover-proyecto');
          console.log('🖱️ Mouseover en proyecto');
        });
  
        div.addEventListener('mouseout', function () {
          div.classList.remove('hover-proyecto');
          console.log('👋 Mouseout en proyecto');
        });
      });
    } else {
      console.warn('⚠️ No se encontraron elementos .row.project');
    }
  });