const revealItems = document.querySelectorAll('.project, .skill-group');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.14 });

revealItems.forEach((item, index) => {
  item.style.transitionDelay = `${(index % 4) * 70}ms`;
  observer.observe(item);
});

const style = document.createElement('style');
style.textContent = '.project,.skill-group{opacity:0;transform:translateY(18px);transition:opacity .65s ease,transform .65s ease}.project.is-visible,.skill-group.is-visible{opacity:1;transform:translateY(0)}';
document.head.appendChild(style);
