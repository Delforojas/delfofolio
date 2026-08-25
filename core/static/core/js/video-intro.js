(function () {
  'use strict';

  const overlay = document.getElementById('videoIntro');
  const video = document.getElementById('videoIntroMedia');

  if (!overlay || !video) {
    return;
  }

  const fadeDuration = 400;
  let isClosing = false;
  let isClosed = false;

  document.body.classList.add('video-intro-active');

  function finishClose() {
    if (isClosed) {
      return;
    }

    isClosed = true;
    video.pause();
    overlay.hidden = true;
    document.body.classList.remove('video-intro-active');
  }

  function closeIntro() {
    if (isClosing) {
      return;
    }

    isClosing = true;
    overlay.classList.add('is-closing');
    overlay.setAttribute('aria-hidden', 'true');

    window.setTimeout(finishClose, fadeDuration);
  }

  overlay.addEventListener('click', closeIntro);
  video.addEventListener('ended', closeIntro);
  overlay.addEventListener('transitionend', function (event) {
    if (event.target === overlay && event.propertyName === 'opacity') {
      finishClose();
    }
  });
})();
