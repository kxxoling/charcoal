(function() {
  var active;
  var path = document.location.pathname;

  if (path.startsWith('/a/')) {
    active = 'articles';
  } else if (path.startsWith('/g/')) {
    active = 'galleries';
  } else if (path.startsWith('/l/')) {
    active = 'links';
  } else if (path.startsWith('/v/')) {
    active = 'videos';
  } else {
    active = 'home';
  }

  var activeNode = document.querySelector('.header .nav-left .nav-' + active);
  activeNode.classList.add('is-active');
})()
