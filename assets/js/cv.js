document.addEventListener('DOMContentLoaded', function() {
	// Smooth scrolling for navigation links
	const navLinks = document.querySelectorAll('nav a[href^="#"]');
	navLinks.forEach(link => {
		link.addEventListener('click', function(e) {
			e.preventDefault();
			const targetSection = document.querySelector(this.getAttribute('href'));
			if (!targetSection) return;
			targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
			navLinks.forEach(navLink => navLink.classList.remove('active'));
			this.classList.add('active');
		});
	});

	// A shared view switch for work experience and education
	const resumeViewToggle = document.querySelector('.resume-view-toggle');
	const resumeLists = [
		document.getElementById('experience-list'),
		document.getElementById('education-list')
	].filter(Boolean);

	function updateResumeToggleLabel(timelineActive) {
		if (!resumeViewToggle) return;
		const isEnglish = document.documentElement.lang === 'en';
		const label = isEnglish
			? (timelineActive ? 'Timeline view active for experience and education; switch to list view' : 'List view for experience and education; switch to timeline view')
			: (timelineActive ? 'Timeline-Ansicht für Berufserfahrung und Bildung aktiv; zur Listenansicht wechseln' : 'Listenansicht für Berufserfahrung und Bildung; zur Timeline-Ansicht wechseln');
		resumeViewToggle.setAttribute('aria-label', label);
		resumeViewToggle.setAttribute('title', label);
	}

	if (resumeViewToggle && resumeLists.length) {
		resumeViewToggle.addEventListener('click', () => {
			const timelineActive = !resumeLists[0].classList.contains('is-timeline');
			resumeLists.forEach(list => list.classList.toggle('is-timeline', timelineActive));
			const icon = resumeViewToggle.querySelector('i');
			icon.classList.toggle('fa-code-branch', timelineActive);
			icon.classList.toggle('fa-list', !timelineActive);
			resumeViewToggle.setAttribute('aria-pressed', String(timelineActive));
			updateResumeToggleLabel(timelineActive);
		});
		updateResumeToggleLabel(false);
	}

	// Add fade-in animation to sections without writing inline styles.
	const sections = document.querySelectorAll('.section');
	const observerOptions = {
		threshold: 0.1,
		rootMargin: '0px 0px -50px 0px'
	};
	const observer = new IntersectionObserver(function(entries) {
		entries.forEach(entry => {
			if (entry.isIntersecting) entry.target.classList.remove('fade-in-pending');
		});
	}, observerOptions);
	sections.forEach(section => {
		section.classList.add('fade-in-pending');
		observer.observe(section);
	});

	// Navigation highlighting on scroll
	function updateActiveNavigation() {
		const scrollPos = window.scrollY + 200;
		sections.forEach(section => {
			if (scrollPos >= section.offsetTop && scrollPos < section.offsetTop + section.offsetHeight) {
				navLinks.forEach(link => link.classList.remove('active'));
				const activeLink = document.querySelector(`nav a[href="#${section.id}"]`);
				if (activeLink) activeLink.classList.add('active');
			}
		});
	}
	window.addEventListener('scroll', updateActiveNavigation);
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
