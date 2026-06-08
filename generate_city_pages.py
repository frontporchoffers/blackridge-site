#!/usr/bin/env python3
"""
Programmatic SEO: Generate city-specific landing pages for Black Ridge Contracting.
Each page targets "[service] in [city] Iowa" keywords with unique content.
"""

import os

CITIES = [
    {"name": "Ankeny", "zip": "50021", "pop": "72,000+", "desc": "our hometown", "detail": "As Ankeny's hometown contractor, we know every neighborhood — from Prairie Trail to North Ankeny. Our crew is just minutes away, which means faster response times and a team that truly cares about keeping Ankeny homes looking their best."},
    {"name": "Des Moines", "zip": "50309", "pop": "215,000+", "desc": "Iowa's capital city", "detail": "From the East Village to South Side, Des Moines homeowners deserve contractors who show up on time and do the work right. Black Ridge Contracting has completed dozens of projects across Des Moines — from storm damage repairs downtown to full exterior renovations in Beaverdale."},
    {"name": "West Des Moines", "zip": "50265", "pop": "68,000+", "desc": "one of Iowa's fastest-growing cities", "detail": "West Des Moines homes — from Valley Junction to Jordan Creek — face the same Iowa weather challenges. Our team has handled roofing, siding, and concrete projects across WDM, and we know the building standards and HOA requirements in the area."},
    {"name": "Urbandale", "zip": "50322", "pop": "45,000+", "desc": "a thriving Des Moines suburb", "detail": "Urbandale homeowners take pride in their properties, and so do we. Whether you are in the Walnut Creek area or near Merle Hay, our crew delivers the same quality work that has earned us a 4.9-star rating across Central Iowa."},
    {"name": "Johnston", "zip": "50131", "pop": "24,000+", "desc": "a growing community in Polk County", "detail": "Johnston has seen tremendous growth over the past decade, and many homes need exterior updates to keep up. From new construction roofing in Tiffin Heights to siding replacements near Beaver Creek, we serve Johnston homeowners with the same care we put into our own Ankeny neighbors' homes."},
    {"name": "Waukee", "zip": "50263", "pop": "25,000+", "desc": "one of Iowa's fastest-growing cities", "detail": "Waukee's rapid growth means more homes that need quality exterior work. From the Kettlestone development to established neighborhoods off Hickman Road, Black Ridge Contracting brings honest pricing and expert craftsmanship to Waukee homeowners."},
    {"name": "Clive", "zip": "50325", "pop": "18,000+", "desc": "a well-established Des Moines suburb", "detail": "Clive is known for its beautiful neighborhoods and well-maintained homes. Our team has completed siding installations, roof replacements, and concrete work throughout Clive — from the Greenbelt Trail area to neighborhoods near University Avenue."},
    {"name": "Grimes", "zip": "50111", "pop": "16,000+", "desc": "a fast-growing northern suburb", "detail": "Grimes continues to grow rapidly, and new homeowners need trusted contractors they can count on. Whether you are in the South Lakes area or along SE Gateway Drive, Black Ridge delivers quality roofing, siding, gutter, and concrete services to Grimes families."},
    {"name": "Polk City", "zip": "50226", "pop": "5,000+", "desc": "a charming community near Saylorville Lake", "detail": "Polk City homeowners enjoy small-town living close to nature. The proximity to Saylorville Lake means extra weather exposure for your home's exterior. Black Ridge Contracting helps Polk City families protect their investment with quality roofing, siding, and gutter work built to last."},
    {"name": "Altoona", "zip": "50009", "pop": "20,000+", "desc": "a growing eastern suburb of Des Moines", "detail": "Altoona has grown from a small town to a thriving suburb. Homes throughout Altoona — from the Adventureland area to Spring Creek — benefit from our expert roofing, siding, gutter, and concrete services. We bring the same quality to Altoona that we deliver in our hometown of Ankeny."},
    {"name": "Pleasant Hill", "zip": "50327", "pop": "10,000+", "desc": "a friendly community east of Des Moines", "detail": "Pleasant Hill families deserve a contractor who treats their home with respect. Our crew has served Pleasant Hill homeowners with roof replacements, siding upgrades, and concrete work — always on time, always on budget, and always cleaned up before we leave."},
    {"name": "Bondurant", "zip": "50035", "pop": "8,000+", "desc": "one of Iowa's fastest-growing small cities", "detail": "Bondurant has experienced incredible growth, with new homes and new families moving in every year. Black Ridge Contracting is proud to serve Bondurant homeowners with the same honest, quality-driven approach that has earned us 200+ completed projects across Central Iowa."},
    {"name": "Norwalk", "zip": "50211", "pop": "12,000+", "desc": "a southern Des Moines metro community", "detail": "Norwalk sits on the southern edge of the Des Moines metro, and its homes face the full range of Iowa weather. From hail damage on roofs to cracking concrete driveways, Black Ridge Contracting helps Norwalk homeowners protect and improve their properties with professional exterior services."},
    {"name": "Carlisle", "zip": "50047", "pop": "4,000+", "desc": "a tight-knit community south of Des Moines", "detail": "Carlisle may be smaller, but its homeowners deserve the same quality of work as any Des Moines suburb. We bring full-service roofing, siding, gutter, and concrete work to Carlisle families — with the same free estimates, honest pricing, and clean job sites we are known for."},
    {"name": "Windsor Heights", "zip": "50324", "pop": "5,000+", "desc": "a charming enclave within Des Moines", "detail": "Windsor Heights is known for its character homes and tree-lined streets. Many of these homes need updated roofing, siding, and gutters to stay protected. Black Ridge Contracting brings careful, respectful workmanship to Windsor Heights — because older homes deserve extra attention."},
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Black Ridge Contracting serves {city}, IA with expert roofing, siding, gutter, and concrete services. Family-owned in Ankeny. Free estimates. Call (515) 219-4654.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://blackridgecontractor.com/areas/{slug}">
  <meta property="og:title" content="Roofing, Siding, Gutters & Concrete in {city} IA | Black Ridge Contracting">
  <meta property="og:description" content="Family-owned contractor serving {city}, Iowa. Roofing, siding, gutters, and concrete. 200+ projects completed. Free estimates.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://blackridgecontractor.com/areas/{slug}">
  <meta property="og:image" content="https://blackridgecontractor.com/pictures/Black Ridge Contracting Full Size Photo.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Roofing & Exterior Services in {city} IA | Black Ridge Contracting">
  <meta name="twitter:description" content="Family-owned contractor serving {city}, Iowa. 200+ projects. Free estimates.">
  <title>Roofing, Siding, Gutters & Concrete in {city} IA | Black Ridge Contracting</title>
  <link rel="stylesheet" href="../styles.css">
  <link rel="icon" type="image/webp" href="pictures/Black Ridge Contracting Favicon.webp">

  <!-- JSON-LD: LocalBusiness -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Black Ridge Contracting",
    "description": "Family-owned roofing, siding, gutter, and concrete contractor serving {city}, Iowa and all of Central Iowa.",
    "url": "https://blackridgecontractor.com",
    "telephone": "+1-515-219-4654",
    "email": "drew@blackridgecontractor.com",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Ankeny",
      "addressRegion": "IA",
      "postalCode": "50023",
      "addressCountry": "US"
    }},
    "areaServed": {{
      "@type": "City",
      "name": "{city}",
      "sameAs": "https://en.wikipedia.org/wiki/{city_wiki},_Iowa"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "47",
      "bestRating": "5"
    }}
  }}
  </script>

  <!-- JSON-LD: BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://blackridgecontractor.com/"}},
      {{"@type": "ListItem", "position": 2, "name": "Service Areas", "item": "https://blackridgecontractor.com/areas/"}},
      {{"@type": "ListItem", "position": 3, "name": "{city}, IA"}}
    ]
  }}
  </script>

  <!-- JSON-LD: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "What exterior services does Black Ridge Contracting offer in {city}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "We offer roofing (new construction, replacements, storm damage repair), siding installation (vinyl, fiber cement, engineered wood), gutter services (installation, repair, guards), and concrete work (driveways, sidewalks, patios, steps) throughout {city}, IA."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Does Black Ridge Contracting serve {city} Iowa?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes. Black Ridge Contracting is based in Ankeny, IA and proudly serves {city} and all of Central Iowa. We are typically just a short drive from any project in {city}."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How do I get a free estimate in {city}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Call us at (515) 219-4654 or fill out our online form. We will schedule a free, no-obligation visit to your {city} property, inspect the work needed, and provide a clear written quote — usually within 24 hours."
        }}
      }}
    ]
  }}
  </script>
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <nav class="nav" aria-label="Main navigation">
    <div class="nav-inner">
      <a href="../" class="nav-logo" aria-label="Black Ridge Contracting home"><div class="nav-logo-icon" aria-hidden="true">B</div> Black Ridge</a>
      <div class="nav-links">
        <a href="../">Home</a>
        <div class="nav-dropdown">
          <a href="../#services">Services &#9662;</a>
          <div class="nav-dropdown-menu" role="menu">
            <a href="../services/roofing.html" role="menuitem">Roofing</a>
            <a href="../services/siding.html" role="menuitem">Siding</a>
            <a href="../services/gutters.html" role="menuitem">Gutters</a>
            <a href="../services/concrete.html" role="menuitem">Concrete</a>
          </div>
        </div>
        <a href="../about.html">About</a>
        <a href="../contact.html">Contact</a>
        <a href="tel:5152194654" class="nav-cta">&#9742; (515) 219-4654</a>
      </div>
      <button class="hamburger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </nav>

  <div class="mobile-menu" role="dialog" aria-label="Mobile navigation">
    <a href="../">Home</a>
    <a href="../services/roofing.html">Roofing</a>
    <a href="../services/siding.html">Siding</a>
    <a href="../services/gutters.html">Gutters</a>
    <a href="../services/concrete.html">Concrete</a>
    <a href="../about.html">About</a>
    <a href="../contact.html">Contact</a>
    <a href="tel:5152194654" class="mobile-cta">&#9742; (515) 219-4654</a>
  </div>

  <header class="hero page-hero" role="banner">
    <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&h=900&fit=crop" alt="Beautiful residential home with professional exterior work in {city} Iowa neighborhood" class="hero-bg" width="1600" height="900" loading="eager">
    <div class="hero-overlay" aria-hidden="true"></div>
    <div class="hero-pattern" aria-hidden="true"></div>
    <div class="hero-content">
      <div class="hero-badge">&#128205; Serving {city}, IA &amp; All of Central Iowa</div>
      <h1>Roofing, Siding, Gutters & Concrete in <span class="highlight">{city}, Iowa</span> — Trusted by 200+ Homeowners</h1>
      <p class="hero-sub">Black Ridge Contracting is a family-owned exterior contractor based in Ankeny, serving {city} and {desc} with honest work and fair prices since 2020.</p>
      <div class="hero-buttons">
        <a href="../contact.html" class="btn btn-primary btn-lg">Get a Free Estimate in {city} &#8594;</a>
        <a href="tel:5152194654" class="btn btn-secondary btn-lg">&#9742; Call (515) 219-4654</a>
      </div>
    </div>
  </header>

  <div class="breadcrumbs" aria-label="Breadcrumb navigation">
    <div class="container">
      <div class="breadcrumbs-inner">
        <a href="../">Home</a>
        <span class="separator" aria-hidden="true">&#8250;</span>
        <span>Service Areas</span>
        <span class="separator" aria-hidden="true">&#8250;</span>
        <span aria-current="page">{city}, IA</span>
      </div>
    </div>
  </div>

  <div class="trust-bar">
    <div class="container">
      <div class="trust-bar-inner">
        <div class="trust-item"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#f5a623"/></svg> 4.9/5 Google Rating</div>
        <div class="trust-divider" aria-hidden="true"></div>
        <div class="trust-item"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z" fill="#22c55e"/><path d="M10 15.5l-3.5-3.5 1.41-1.41L10 12.67l5.59-5.59L17 8.5l-7 7z" fill="white"/></svg> Licensed &amp; Insured</div>
        <div class="trust-divider" aria-hidden="true"></div>
        <div class="trust-item"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="3" fill="#005a8c"/><text x="12" y="14" text-anchor="middle" fill="white" font-size="7" font-weight="bold">BBB</text></svg> BBB Accredited</div>
        <div class="trust-divider" aria-hidden="true"></div>
        <div class="trust-item"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="#e94d1a"/></svg> 200+ Projects Completed</div>
      </div>
    </div>
  </div>

  <main id="main">

    <section class="section" aria-labelledby="city-about-title">
      <div class="container">
        <div class="split">
          <div class="split-content reveal">
            <span class="section-label">Serving {city}, IA</span>
            <h2 id="city-about-title">Your Trusted Exterior Contractor in {city}, Iowa</h2>
            <p>{detail}</p>
            <p>We handle every part of your home's exterior: roofing, siding, gutters, and concrete. Every project comes with a free estimate, honest pricing, and a clean job site. That is the Black Ridge promise — whether you are in {city} or anywhere else in Central Iowa.</p>
            <ul>
              <li><span class="check-icon" aria-hidden="true">&#10003;</span> Family-owned, based just minutes away in Ankeny</li>
              <li><span class="check-icon" aria-hidden="true">&#10003;</span> Fully licensed and insured in Iowa</li>
              <li><span class="check-icon" aria-hidden="true">&#10003;</span> Free, no-pressure estimates</li>
              <li><span class="check-icon" aria-hidden="true">&#10003;</span> 24/7 emergency storm damage response</li>
            </ul>
            <a href="../contact.html" class="btn btn-primary">Get a Free Estimate &#8594;</a>
          </div>
          <div class="split-img reveal reveal-delay-2">
            <img src="https://images.unsplash.com/photo-1621905252507-b35492cc74b4?w=800&h=600&fit=crop" alt="Black Ridge Contracting crew completing exterior renovation on residential property in {city} Iowa" width="800" height="600" loading="lazy">
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" aria-labelledby="city-services-title">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Our Services in {city}</span>
          <h2 id="city-services-title" class="section-title">Exterior Services We Provide in {city}, Iowa</h2>
          <p class="section-subtitle">From your roof to your driveway, Black Ridge handles it all for {city} homeowners.</p>
        </div>
        <div class="card-grid card-grid-4">
          <a href="../services/roofing.html" class="card card-img reveal reveal-delay-1" aria-label="Roofing services in {city}">
            <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=600&h=400&fit=crop" alt="Professional roof installation on home in {city} Iowa by Black Ridge Contracting" width="600" height="400" loading="lazy">
            <div class="card-img-body">
              <h3>Roofing in {city}</h3>
              <p>New roofs, replacements, storm damage repair, and inspections for {city} homeowners.</p>
              <span class="card-link">Learn about roofing &#8594;</span>
            </div>
          </a>
          <a href="../services/siding.html" class="card card-img reveal reveal-delay-2" aria-label="Siding services in {city}">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&h=400&fit=crop" alt="New siding installation on residential home in {city} Iowa" width="600" height="400" loading="lazy">
            <div class="card-img-body">
              <h3>Siding in {city}</h3>
              <p>Vinyl, fiber cement, and engineered wood siding to protect and beautify your {city} home.</p>
              <span class="card-link">Explore siding options &#8594;</span>
            </div>
          </a>
          <a href="../services/gutters.html" class="card card-img reveal reveal-delay-3" aria-label="Gutter services in {city}">
            <img src="https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=600&h=400&fit=crop" alt="Seamless gutter system installed on home in {city} Iowa" width="600" height="400" loading="lazy">
            <div class="card-img-body">
              <h3>Gutters in {city}</h3>
              <p>Gutter installation, repair, and guards to protect your {city} home's foundation.</p>
              <span class="card-link">See gutter solutions &#8594;</span>
            </div>
          </a>
          <a href="../services/concrete.html" class="card card-img reveal reveal-delay-4" aria-label="Concrete services in {city}">
            <img src="https://images.unsplash.com/photo-1590496793929-36417d3117de?w=600&h=400&fit=crop" alt="Fresh concrete driveway poured at home in {city} Iowa" width="600" height="400" loading="lazy">
            <div class="card-img-body">
              <h3>Concrete in {city}</h3>
              <p>Driveways, sidewalks, patios, and steps for {city} homes. Removal and replacement.</p>
              <span class="card-link">Get a concrete quote &#8594;</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="city-faq-title">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Common Questions</span>
          <h2 id="city-faq-title" class="section-title">Questions {city} Homeowners Ask Us</h2>
        </div>
        <div class="faq-list reveal">
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">What exterior services does Black Ridge Contracting offer in {city}?</button>
            <div class="faq-answer" role="region"><p>We offer roofing (new construction, replacements, storm damage repair), siding installation (vinyl, fiber cement, engineered wood), gutter services (installation, repair, guards), and concrete work (driveways, sidewalks, patios, steps) throughout {city}, IA.</p></div>
          </div>
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">Does Black Ridge Contracting serve {city}, Iowa?</button>
            <div class="faq-answer" role="region"><p>Yes. Black Ridge Contracting is based in Ankeny, IA and proudly serves {city} and all of Central Iowa. We are typically just a short drive from any project in {city}.</p></div>
          </div>
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">How do I get a free estimate in {city}?</button>
            <div class="faq-answer" role="region"><p>Call us at (515) 219-4654 or fill out our online form. We will schedule a free, no-obligation visit to your {city} property, inspect the work needed, and provide a clear written quote — usually within 24 hours.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" aria-labelledby="other-areas-title">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">More Service Areas</span>
          <h2 id="other-areas-title" class="section-title">We Also Serve These Central Iowa Cities</h2>
        </div>
        <div class="service-area-grid reveal">
          {other_cities_html}
        </div>
      </div>
    </section>

    <section class="cta-banner" aria-labelledby="city-cta-title">
      <div class="container">
        <h2 id="city-cta-title">Ready to Start Your {city} Project? Get a Free Estimate.</h2>
        <p>Join 200+ Central Iowa homeowners who trust Black Ridge Contracting. Call today or fill out our form — we respond within 24 hours.</p>
        <a href="../contact.html" class="btn btn-primary btn-lg">Get Your Free Estimate &#8594;</a>
        <a href="tel:5152194654" class="btn btn-secondary btn-lg">&#9742; Call (515) 219-4654</a>
      </div>
    </section>
  </main>

  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo"><div class="nav-logo-icon" aria-hidden="true">B</div> Black Ridge Contracting</div>
          <p>Family-owned exterior contractor based in Ankeny, IA. Started by a father and son in 2020, now proudly serving all of Central Iowa with quality roofing, siding, gutter, and concrete work.</p>
          <div class="social-links"><a href="https://www.facebook.com/groups/1256471666659865" class="social-link" aria-label="Follow Black Ridge Contracting on Facebook" target="_blank" rel="noopener">f</a></div>
        </div>
        <div>
          <h4>Services</h4>
          <ul class="footer-links">
            <li><a href="../services/roofing.html">Roofing</a></li>
            <li><a href="../services/siding.html">Siding</a></li>
            <li><a href="../services/gutters.html">Gutters</a></li>
            <li><a href="../services/concrete.html">Concrete</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul class="footer-links">
            <li><a href="../about.html">About Us</a></li>
            <li><a href="../contact.html">Contact</a></li>
            <li><a href="../contact.html">Free Estimate</a></li>
          </ul>
        </div>
        <div>
          <h3>Contact Us</h3>
          <div class="footer-contact-item"><span class="footer-contact-icon" aria-hidden="true">&#9742;</span><a href="tel:5152194654">(515) 219-4654</a></div>
          <div class="footer-contact-item"><span class="footer-contact-icon" aria-hidden="true">&#9993;</span><a href="mailto:drew@blackridgecontractor.com">drew@blackridgecontractor.com</a></div>
          <div class="footer-contact-item"><span class="footer-contact-icon" aria-hidden="true">&#128205;</span><span>Ankeny, IA 50021</span></div>
          <div class="footer-contact-item"><span class="footer-contact-icon" aria-hidden="true">&#128337;</span><span>Mon-Fri 7am-6pm, Sat 8am-2pm</span></div>
        </div>
      </div>
      <div class="footer-bottom">&copy; 2026 Black Ridge Contracting. All rights reserved. Family-owned in Ankeny, Iowa.</div>
    </div>
  </footer>

  <script>
    const reveals=document.querySelectorAll('.reveal');const observer=new IntersectionObserver((entries)=>{{entries.forEach(entry=>{{if(entry.isIntersecting)entry.target.classList.add('visible');}});}},{{threshold:0.1}});reveals.forEach(el=>observer.observe(el));
    window.addEventListener('scroll',()=>{{document.querySelector('.nav').classList.toggle('scrolled',window.scrollY>50);}});
    const hamburger=document.querySelector('.hamburger');const mobileMenu=document.querySelector('.mobile-menu');hamburger.addEventListener('click',()=>{{hamburger.classList.toggle('active');mobileMenu.classList.toggle('open');hamburger.setAttribute('aria-expanded',mobileMenu.classList.contains('open'));document.body.style.overflow=mobileMenu.classList.contains('open')?'hidden':'';}});
    mobileMenu.querySelectorAll('a').forEach(link=>{{link.addEventListener('click',()=>{{hamburger.classList.remove('active');mobileMenu.classList.remove('open');hamburger.setAttribute('aria-expanded','false');document.body.style.overflow='';}});}});
    document.querySelectorAll('.faq-question').forEach(btn=>{{btn.addEventListener('click',()=>{{const item=btn.parentElement;const isOpen=item.classList.contains('open');document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'));document.querySelectorAll('.faq-question').forEach(b=>b.setAttribute('aria-expanded','false'));if(!isOpen){{item.classList.add('open');btn.setAttribute('aria-expanded','true');}}}});}});
  </script>
</body>
</html>"""

output_dir = "/Users/Drew/Desktop/Claude/claude-skills-main/local-seo-agency/brc-site/areas"
os.makedirs(output_dir, exist_ok=True)

for city in CITIES:
    slug = city["name"].lower().replace(" ", "-")
    city_wiki = city["name"].replace(" ", "_")

    # Build other cities HTML (exclude current city)
    other_cities = [c for c in CITIES if c["name"] != city["name"]]
    other_html = "\n          ".join(
        f'<a href="{c["name"].lower().replace(" ", "-")}.html" class="service-area-tag">{c["name"]}</a>'
        for c in other_cities
    )

    html = TEMPLATE.format(
        city=city["name"],
        slug=slug,
        zip=city["zip"],
        pop=city["pop"],
        desc=city["desc"],
        detail=city["detail"],
        city_wiki=city_wiki,
        other_cities_html=other_html,
    )

    filepath = os.path.join(output_dir, f"{slug}.html")
    with open(filepath, "w") as f:
        f.write(html)
    print(f"Created: {filepath}")

print(f"\nDone! Generated {len(CITIES)} city landing pages.")
