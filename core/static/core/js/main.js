/**
 * Portfolio Design System JavaScript
 * Handles Theme Toggling (Light/Dark mode) & Mobile Navigation interactions
 */

(function () {
    'use strict';

    const STORAGE_KEY = 'portfolio-theme';

    /**
     * Get preferred theme from localStorage or system preference.
     * @returns {'light'|'dark'}
     */
    function getPreferredTheme() {
        const storedTheme = localStorage.getItem(STORAGE_KEY);
        if (storedTheme) {
            return storedTheme;
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    /**
     * Apply theme to root html element and update toggle button icon.
     * @param {'light'|'dark'} theme
     */
    function setTheme(theme) {
        document.documentElement.setAttribute('data-bs-theme', theme);
        updateToggleIcon(theme);
    }

    /**
     * Updates theme toggle button icon and accessible aria-label.
     * @param {'light'|'dark'} theme
     */
    function updateToggleIcon(theme) {
        const toggleBtn = document.getElementById('theme-toggle-btn');
        if (!toggleBtn) return;

        const icon = toggleBtn.querySelector('i');
        if (icon) {
            if (theme === 'dark') {
                icon.className = 'bi bi-sun-fill text-warning';
                toggleBtn.setAttribute('aria-label', 'Switch to light mode');
                toggleBtn.setAttribute('title', 'Switch to light mode');
            } else {
                icon.className = 'bi bi-moon-stars-fill text-secondary';
                toggleBtn.setAttribute('aria-label', 'Switch to dark mode');
                toggleBtn.setAttribute('title', 'Switch to dark mode');
            }
        }
    }

    // Initialize theme immediately on page load
    const currentTheme = getPreferredTheme();
    setTheme(currentTheme);

    document.addEventListener('DOMContentLoaded', function () {
        // Wire up toggle button
        const toggleBtn = document.getElementById('theme-toggle-btn');
        if (toggleBtn) {
            updateToggleIcon(document.documentElement.getAttribute('data-bs-theme') || 'light');
            toggleBtn.addEventListener('click', function () {
                const activeTheme = document.documentElement.getAttribute('data-bs-theme');
                const newTheme = activeTheme === 'dark' ? 'light' : 'dark';
                localStorage.setItem(STORAGE_KEY, newTheme);
                setTheme(newTheme);
            });
        }

        // Listen for system theme changes if user hasn't set an explicit preference
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
            if (!localStorage.getItem(STORAGE_KEY)) {
                setTheme(e.matches ? 'dark' : 'light');
            }
        });

        // Close mobile navbar on link click
        const navLinks = document.querySelectorAll('.navbar-custom .nav-link:not(.dropdown-toggle)');
        const navbarCollapse = document.getElementById('navbarResponsive');
        if (navbarCollapse && window.bootstrap) {
            navLinks.forEach(function (link) {
                link.addEventListener('click', function () {
                    const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                    if (bsCollapse && navbarCollapse.classList.contains('show')) {
                        bsCollapse.hide();
                    }
                });
            });
        }

        // Certificate Lightbox Modal handler
        const certLightboxModalEl = document.getElementById('certificateLightboxModal');
        if (certLightboxModalEl && window.bootstrap) {
            const certModalImg = document.getElementById('certModalImage');
            const certModalTitle = document.getElementById('certModalTitle');
            const certModalOrg = document.getElementById('certModalOrg');
            const certModalDate = document.getElementById('certModalDate');
            const certModalDownloadBtn = document.getElementById('certModalDownloadBtn');

            document.querySelectorAll('[data-cert-modal="true"]').forEach(function (trigger) {
                trigger.addEventListener('click', function (e) {
                    e.preventDefault();
                    const imgUrl = this.getAttribute('data-cert-img');
                    const title = this.getAttribute('data-cert-title');
                    const org = this.getAttribute('data-cert-org');
                    const date = this.getAttribute('data-cert-date');

                    if (certModalImg && imgUrl) {
                        certModalImg.src = imgUrl;
                        certModalImg.alt = title || 'Certificate';
                    }
                    if (certModalTitle) certModalTitle.textContent = title || 'Certificate Preview';
                    if (certModalOrg) certModalOrg.textContent = org || '';
                    if (certModalDate) certModalDate.textContent = date || '';
                    if (certModalDownloadBtn && imgUrl) {
                        certModalDownloadBtn.href = imgUrl;
                    }

                    const modalInstance = bootstrap.Modal.getOrCreateInstance(certLightboxModalEl);
                    modalInstance.show();
                });
            });
        }

        // Client-side Certificate category filtering
        const certFilterButtons = document.querySelectorAll('[data-cert-filter]');
        const certItems = document.querySelectorAll('.cert-grid-item');
        if (certFilterButtons.length > 0 && certItems.length > 0) {
            certFilterButtons.forEach(function (btn) {
                btn.addEventListener('click', function (e) {
                    // If running with standard anchor navigation, allow default or handle via JS
                    const filterValue = this.getAttribute('data-cert-filter');
                    certFilterButtons.forEach(b => b.classList.remove('active-filter', 'btn-primary-custom'));
                    certFilterButtons.forEach(b => b.classList.add('btn-outline-custom'));
                    this.classList.remove('btn-outline-custom');
                    this.classList.add('active-filter', 'btn-primary-custom');

                    certItems.forEach(function (item) {
                        const itemCat = item.getAttribute('data-category');
                        if (filterValue === 'all' || itemCat === filterValue) {
                            item.style.display = '';
                        } else {
                            item.style.display = 'none';
                        }
                    });
                });
            });
        }

        // Sticky Navbar Glassmorphism on Scroll
        const navbar = document.querySelector('.navbar-custom');
        function handleNavbarScroll() {
            if (!navbar) return;
            if (window.scrollY > 20) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        }
        window.addEventListener('scroll', handleNavbarScroll, { passive: true });
        handleNavbarScroll();

        // Typing Effect for Hero Title
        const typingEl = document.getElementById('hero-typing-text');
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (typingEl && !prefersReducedMotion) {
            let titles = [];
            try {
                titles = JSON.parse(typingEl.getAttribute('data-titles') || '[]');
            } catch (err) {
                titles = [];
            }

            if (titles.length > 0) {
                let titleIndex = 0;
                let charIndex = titles[0].length;
                let isDeleting = true;
                const typingSpeed = 90;
                const deleteSpeed = 45;
                const pauseEnd = 2400;
                const pauseStart = 400;

                function typeLoop() {
                    const currentTitle = titles[titleIndex];

                    if (isDeleting) {
                        charIndex--;
                        typingEl.textContent = currentTitle.substring(0, charIndex);
                        if (charIndex <= 0) {
                            isDeleting = false;
                            titleIndex = (titleIndex + 1) % titles.length;
                            setTimeout(typeLoop, pauseStart);
                            return;
                        }
                        setTimeout(typeLoop, deleteSpeed);
                    } else {
                        charIndex++;
                        typingEl.textContent = currentTitle.substring(0, charIndex);
                        if (charIndex >= currentTitle.length) {
                            isDeleting = true;
                            setTimeout(typeLoop, pauseEnd);
                            return;
                        }
                        setTimeout(typeLoop, typingSpeed);
                    }
                }

                // Initial pause before starting typing cycle
                setTimeout(typeLoop, pauseEnd);
            }
        }

        // Scroll Reveal Animation (IntersectionObserver)
        const revealElements = document.querySelectorAll('.reveal-on-scroll');
        if (revealElements.length > 0 && 'IntersectionObserver' in window && !prefersReducedMotion) {
            const revealObserver = new IntersectionObserver(function (entries, observer) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.12,
                rootMargin: '0px 0px -30px 0px'
            });

            revealElements.forEach(function (el) {
                revealObserver.observe(el);
            });
        } else {
            // Immediate display if reduced motion or no IntersectionObserver
            revealElements.forEach(function (el) {
                el.classList.add('is-revealed');
            });
        }

        // Back to Top Button
        const backToTopBtn = document.getElementById('back-to-top-btn');
        if (backToTopBtn) {
            function handleBackToTopVisibility() {
                if (window.scrollY > 300) {
                    backToTopBtn.classList.add('is-visible');
                } else {
                    backToTopBtn.classList.remove('is-visible');
                }
            }
            window.addEventListener('scroll', handleBackToTopVisibility, { passive: true });
            handleBackToTopVisibility();

            backToTopBtn.addEventListener('click', function () {
                window.scrollTo({
                    top: 0,
                    behavior: prefersReducedMotion ? 'auto' : 'smooth'
                });
            });
        }

        console.log('Portfolio design system initialized. Current theme:', document.documentElement.getAttribute('data-bs-theme'));
    });
})();
