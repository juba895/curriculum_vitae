document.addEventListener('DOMContentLoaded', function() {
	// Smooth scrolling for navigation links
	const navLinks = document.querySelectorAll('nav a[href^="#"]');
	const siteNavWrap = document.querySelector('.site-nav-wrap');
	const siteNavToggle = document.querySelector('.site-nav-toggle');
	function setMobileMenuOpen(isOpen) {
		if (!siteNavWrap || !siteNavToggle) return;
		siteNavWrap.classList.toggle('is-open', isOpen);
		document.body.classList.toggle('mobile-nav-open', isOpen);
		siteNavToggle.setAttribute('aria-expanded', String(isOpen));
		const isEnglish = document.documentElement.lang === 'en';
		siteNavToggle.setAttribute('aria-label', isEnglish
			? (isOpen ? 'Close menu' : 'Open menu')
			: (isOpen ? 'Menü schließen' : 'Menü öffnen'));
		const icon = siteNavToggle.querySelector('i');
		if (icon) {
			icon.classList.toggle('fa-bars', !isOpen);
			icon.classList.toggle('fa-xmark', isOpen);
		}
	}
	if (siteNavToggle) {
		siteNavToggle.addEventListener('click', () => {
			setMobileMenuOpen(siteNavToggle.getAttribute('aria-expanded') !== 'true');
		});
		document.addEventListener('keydown', event => {
			if (event.key === 'Escape' && siteNavToggle.getAttribute('aria-expanded') === 'true') {
				setMobileMenuOpen(false);
				siteNavToggle.focus();
			}
		});
		document.addEventListener('click', event => {
			if (siteNavWrap && !siteNavWrap.contains(event.target)) setMobileMenuOpen(false);
		});
		window.addEventListener('resize', () => {
			if (window.matchMedia('(min-width: 601px)').matches) setMobileMenuOpen(false);
		});
	}
	navLinks.forEach(link => {
		link.addEventListener('click', function(e) {
			e.preventDefault();
			const targetSection = document.querySelector(this.getAttribute('href'));
			if (!targetSection) return;
			const behavior = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
			const closeDrawerFirst = siteNavToggle
				&& siteNavToggle.getAttribute('aria-expanded') === 'true'
				&& window.matchMedia('(max-width: 600px)').matches;
			navLinks.forEach(navLink => navLink.classList.remove('active'));
			this.classList.add('active');
			setMobileMenuOpen(false);
			if (closeDrawerFirst) {
				const drawerCloseDelay = behavior === 'smooth' ? 400 : 0;
				window.setTimeout(() => targetSection.scrollIntoView({ behavior, block: 'start' }), drawerCloseDelay);
			} else {
				targetSection.scrollIntoView({ behavior, block: 'start' });
			}
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
		// Keep the initially visible hero from flashing out before the observer runs.
		if (section.id === 'about') return;
		section.classList.add('fade-in-pending');
		observer.observe(section);
	});

	// Cross-fade the large hero portrait into the compact sticky-header avatar.
	const heroPortrait = document.querySelector('.hero__portrait');
	const headerAvatar = document.querySelector('.site-header .avatar');
	const siteHeader = document.querySelector('.site-header');
	if (heroPortrait && headerAvatar && siteHeader) {
		let portraitDocumentCenter = 0;
		const measurePortrait = () => {
			const rect = heroPortrait.getBoundingClientRect();
			portraitDocumentCenter = rect.top + window.scrollY + rect.height / 2;
		};
		const updateAvatarTransfer = () => {
			const headerCenter = headerAvatar.getBoundingClientRect().top + headerAvatar.getBoundingClientRect().height / 2;
			const distance = portraitDocumentCenter - headerCenter;
			const progress = distance > 0
				? Math.min(1, Math.max(0, window.scrollY / distance))
				: 0;
			document.documentElement.style.setProperty('--avatar-transfer', progress.toFixed(3));
		};
		measurePortrait();
		updateAvatarTransfer();
		window.addEventListener('resize', () => {
			measurePortrait();
			updateAvatarTransfer();
		});
		window.addEventListener('scroll', updateAvatarTransfer, { passive: true });
	}

	// Navigation highlighting on scroll
	function updateActiveNavigation() {
		const scrollPos = window.scrollY + 200;
		sections.forEach(section => {
			if (scrollPos >= section.offsetTop && scrollPos < section.offsetTop + section.offsetHeight) {
				navLinks.forEach(link => link.classList.remove('active'));
				const activeLink = document.querySelector(`nav a[href="#${section.id}"]`);
				if (activeLink) {
					activeLink.classList.add('active');
					revealNavigationLink(activeLink);
				}
			}
		});
	}
	window.addEventListener('scroll', updateActiveNavigation);
	updateActiveNavigation();

	// Lightbox for avatar
	const avatars = document.querySelectorAll('.site-header .avatar, .hero__portrait');
	const lightbox = document.getElementById('avatarLightbox');
	if (avatars.length && lightbox) {
		avatars.forEach(avatar => avatar.addEventListener('click', () => lightbox.classList.add('active')));
		lightbox.addEventListener('click', () => lightbox.classList.remove('active'));
		document.addEventListener('keydown', e => {
			if (e.key === 'Escape') lightbox.classList.remove('active');
		});
	}
});
