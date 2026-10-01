document.addEventListener('DOMContentLoaded', function() {
	// Smooth scrolling for navigation links
	const navLinks = document.querySelectorAll('nav a[href^="#"]');
	navLinks.forEach(link => {
		link.addEventListener('click', function(e) {
			e.preventDefault();
			const targetId = this.getAttribute('href');
			const targetSection = document.querySelector(targetId);
			if (targetSection) {
				targetSection.scrollIntoView({
					behavior: 'smooth',
					block: 'start'
				});

				// Update active nav item
				navLinks.forEach(navLink => navLink.classList.remove('active'));
				this.classList.add('active');
			}
		});
	});

	// A shared view switch for work experience and education
	const resumeViewToggle = document.querySelector('.resume-view-toggle');
	const resumeLists = [
		document.getElementById('experience-list'),
		document.getElementById('education-list')
	].filter(Boolean);

	if (resumeViewToggle && resumeLists.length) {
		resumeViewToggle.addEventListener('click', () => {
			const timelineActive = !resumeLists[0].classList.contains('is-timeline');
			resumeLists.forEach(list => list.classList.toggle('is-timeline', timelineActive));

			const icon = resumeViewToggle.querySelector('i');
			icon.classList.toggle('fa-code-branch', timelineActive);
			icon.classList.toggle('fa-list', !timelineActive);

			const label = timelineActive
				? 'Timeline-Ansicht für Berufserfahrung und Bildung aktiv; zur Listenansicht wechseln'
				: 'Listenansicht für Berufserfahrung und Bildung aktiv; zur Timeline-Ansicht wechseln';
			resumeViewToggle.setAttribute('aria-pressed', String(timelineActive));
			resumeViewToggle.setAttribute('aria-label', label);
			resumeViewToggle.setAttribute('title', label);
		});
	}

	// Add fade-in animation to sections without writing inline styles.
	const sections = document.querySelectorAll('.section');
	const observerOptions = {
		threshold: 0.1,
		rootMargin: '0px 0px -50px 0px'
	};

	const observer = new IntersectionObserver(function(entries) {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				entry.target.classList.remove('fade-in-pending');
			}
		});
	}, observerOptions);

	sections.forEach(section => {
		section.classList.add('fade-in-pending');
		observer.observe(section);
	});

	// Navigation highlighting on scroll
	function updateActiveNavigation() {
		const scrollPos = window.scrollY + 200; // Offset for better detection

		sections.forEach(section => {
			const sectionTop = section.offsetTop;
			const sectionHeight = section.offsetHeight;
			const sectionId = section.getAttribute('id');

			if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
				// Remove active class from all nav links
				navLinks.forEach(link => link.classList.remove('active'));

				// Add active class to current section's nav link
				const activeLink = document.querySelector(`nav a[href="#${sectionId}"]`);
				if (activeLink) {
					activeLink.classList.add('active');
				}
			}
		});
	}

	// Listen for scroll events
	window.addEventListener('scroll', updateActiveNavigation);

	// Initial call to set correct active state
	updateActiveNavigation();

	// Lightbox for avatar
	const avatar = document.querySelector('.sidebar .avatar');
	const lightbox = document.getElementById('avatarLightbox');
	if (avatar && lightbox) {
		avatar.addEventListener('click', () => lightbox.classList.add('active'));
		lightbox.addEventListener('click', () => lightbox.classList.remove('active'));
		document.addEventListener('keydown', e => {
			if (e.key === 'Escape') lightbox.classList.remove('active');
		});
	}
});
