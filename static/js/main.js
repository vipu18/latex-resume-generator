// ── Entry counters ──────────────────────────────────────────────
const counters = {};

// ── Entry templates ─────────────────────────────────────────────
const templates = {
  education: (id) => `
    <div class="entry-card" data-entry="education" id="education-entry-${id}">
      <div class="entry-header">
        <h4>Education #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('education-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid two-col">
        <div class="form-group"><label>Institution</label>
          <input type="text" data-field="institution" value="Stanford University" placeholder="University Name" /></div>
        <div class="form-group"><label>Location</label>
          <input type="text" data-field="location" value="Stanford, CA" placeholder="City, State" /></div>
        <div class="form-group"><label>Degree</label>
          <input type="text" data-field="degree" value="Bachelor of Science in Computer Science" placeholder="Degree / Major" /></div>
        <div class="form-group"><label>CGPA</label>
          <input type="text" data-field="cgpa" value="7.9" placeholder="8.5" /></div>
        <div class="form-group"><label>Duration</label>
          <input type="text" data-field="duration" value="September 2018 - June 2022" placeholder="Sep 2018 – Jun 2022" /></div>
        <div class="form-group"><label>Courses (comma separated)</label>
          <input type="text" data-field="courses" value="Algorithms, Data Structures, Machine Learning, Web Development" placeholder="Algorithms, …" /></div>
      </div>
    </div>`,

  experience: (id) => `
    <div class="entry-card" data-entry="experience" id="experience-entry-${id}">
      <div class="entry-header">
        <h4>Experience #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('experience-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid two-col">
        <div class="form-group"><label>Company</label>
          <input type="text" data-field="company" value="Google" placeholder="Company Name" /></div>
        <div class="form-group"><label>Location</label>
          <input type="text" data-field="location" value="Mountain View, CA" placeholder="City, State" /></div>
        <div class="form-group"><label>Role</label>
          <input type="text" data-field="role" value="Software Engineer Intern" placeholder="Your role" /></div>
        <div class="form-group"><label>Duration</label>
          <input type="text" data-field="duration" value="June 2021 - August 2021" placeholder="Jun 2021 – Aug 2021" /></div>
        <div class="form-group"><label>Title</label>
          <input type="text" data-field="detail_title" value="Search Algorithm Optimization" placeholder="Project / Achievement title" /></div>
        <div class="form-group"><label>Description</label>
          <textarea data-field="detail_description" rows="3" placeholder="Describe your work and achievements…">Improved search ranking algorithms by 15% using machine learning.</textarea></div>
      </div>
      <div class="ai-action-row">
        <button class="btn-ai sm" onclick="optimizeExp(${id}, this)">Optimize with AI</button>
      </div>
    </div>`,

  projects: (id) => `
    <div class="entry-card" data-entry="projects" id="projects-entry-${id}">
      <div class="entry-header">
        <h4>Project #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('projects-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid">
        <div class="form-group"><label>Project Title</label>
          <input type="text" data-field="title" value="Resume Generator" placeholder="My Awesome Project" /></div>
        <div class="form-group"><label>Description</label>
          <textarea data-field="description" rows="3" placeholder="Describe the project…">Built a web app to generate LaTeX resumes using AI for grammar and ATS optimization.</textarea></div>
        <div class="form-group"><label>Tech Stack (comma separated)</label>
          <input type="text" data-field="tech_stack" value="LaTeX, Python, AI" placeholder="Python, React, PostgreSQL" /></div>
      </div>
      <div class="ai-action-row">
        <button class="btn-ai sm" onclick="optimizeProj(${id}, this)">Optimize with AI</button>
      </div>
    </div>`,

  publications: (id) => `
    <div class="entry-card" data-entry="publications" id="publications-entry-${id}">
      <div class="entry-header">
        <h4>Publication #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('publications-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid">
        <div class="form-group"><label>Title</label>
          <input type="text" data-field="title" value="AI in Resume Optimization" placeholder="Publication title" /></div>
        <div class="form-group"><label>Description</label>
          <textarea data-field="description" rows="3" placeholder="Brief description…">Research on using AI to improve resume quality and ATS compatibility.</textarea></div>
      </div>
      <div class="ai-action-row">
        <button class="btn-ai sm" onclick="optimizePub(${id}, this)">Optimize with AI</button>
      </div>
    </div>`,

  honors: (id) => `
    <div class="entry-card" data-entry="honors" id="honors-entry-${id}">
      <div class="entry-header">
        <h4>Honor #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('honors-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid two-col">
        <div class="form-group"><label>Title</label>
          <input type="text" data-field="title" value="Student of the Year" placeholder="Award name" /></div>
        <div class="form-group"><label>Year</label>
          <input type="text" data-field="year" value="2025" placeholder="2024" /></div>
      </div>
    </div>`,

  volunteer: (id) => `
    <div class="entry-card" data-entry="volunteer" id="volunteer-entry-${id}">
      <div class="entry-header">
        <h4>Volunteer #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('volunteer-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid two-col">
        <div class="form-group"><label>Organization</label>
          <input type="text" data-field="organization" value="Code for Good" placeholder="Organization Name" /></div>
        <div class="form-group"><label>Location</label>
          <input type="text" data-field="location" value="San Francisco, CA" placeholder="City, State" /></div>
        <div class="form-group"><label>Role</label>
          <input type="text" data-field="role" value="Mentor" placeholder="Your role" /></div>
        <div class="form-group"><label>Duration</label>
          <input type="text" data-field="duration" value="January 2021 - December 2021" placeholder="Jan 2021 – Dec 2021" /></div>
      </div>
    </div>`,

  certificates: (id) => `
    <div class="entry-card" data-entry="certificates" id="certificates-entry-${id}">
      <div class="entry-header">
        <h4>Certificate #${id + 1}</h4>
        <button class="btn-remove" onclick="removeEntry('certificates-entry-${id}')">Remove</button>
      </div>
      <div class="form-grid two-col">
        <div class="form-group"><label>Certificate Name</label>
          <input type="text" data-field="name" value="AWS Certified Cloud Practitioner" placeholder="Certificate Name" /></div>
        <div class="form-group"><label>Issuer</label>
          <input type="text" data-field="issuer" value="Amazon Web Services" placeholder="Issuing Organization" /></div>
        <div class="form-group"><label>Certificate Link</label>
          <input type="text" data-field="link" value="https://aws.amazon.com" placeholder="https://…" /></div>
        <div class="form-group"><label>Year / Duration</label>
          <input type="text" data-field="start_end" value="2023" placeholder="2024" /></div>
      </div>
    </div>`,
};

// ── Entry management ─────────────────────────────────────────────
function addEntry(section) {
  if (!(section in counters)) counters[section] = 0;
  const id = counters[section]++;
  document.getElementById(`${section}-entries`).insertAdjacentHTML('beforeend', templates[section](id));
}

function removeEntry(entryId) {
  document.getElementById(entryId)?.remove();
}

function collectEntries(section) {
  return Array.from(document.querySelectorAll(`[data-entry="${section}"]`)).map(entry => {
    const obj = {};
    entry.querySelectorAll('[data-field]').forEach(el => { obj[el.dataset.field] = el.value.trim(); });
    return obj;
  });
}

// ── Data collection ──────────────────────────────────────────────
function collectFormData() {
  const data = {
    name:      document.getElementById('name').value.trim(),
    email:     document.getElementById('email').value.trim(),
    portfolio: document.getElementById('portfolio').value.trim(),
    mobile:    document.getElementById('mobile').value.trim(),
    github:    document.getElementById('github').value.trim(),
    linkedin:  document.getElementById('linkedin').value.trim(),
  };

  // Education
  const edu = collectEntries('education');
  data.education = edu.length ? edu.map(e => ({
    ...e,
    courses: e.courses ? e.courses.split(',').map(c => c.trim()).filter(Boolean) : [],
  })) : null;

  // Skills
  const skillCats = ['Languages', 'Frameworks', 'Tools', 'Platforms', 'Soft Skills', 'Others'];
  const skills = {};
  skillCats.forEach(cat => {
    const val = document.getElementById('skills-' + cat.replace(' ', '-'))?.value.trim();
    if (val) {
      const items = val.split(',').map(s => s.trim()).filter(Boolean);
      if (items.length) skills[cat] = items;
    }
  });
  data.skills = Object.keys(skills).length ? skills : null;

  // Experience
  const exp = collectEntries('experience');
  data.experience = exp.length ? exp.map(e => ({
    company: e.company, location: e.location, role: e.role, duration: e.duration,
    details: [{ title: e.detail_title, description: e.detail_description }],
  })) : null;

  // Projects
  const proj = collectEntries('projects');
  data.projects = proj.length ? proj.map(e => ({
    title: e.title, description: e.description,
    tech_stack: e.tech_stack ? e.tech_stack.split(',').map(t => t.trim()).filter(Boolean) : [],
  })) : null;

  // Flat sections
  const pubs  = collectEntries('publications');
  const hon   = collectEntries('honors');
  const vol   = collectEntries('volunteer');
  const certs = collectEntries('certificates');
  data.publications = pubs.length  ? pubs  : null;
  data.honors       = hon.length   ? hon   : null;
  data.volunteer    = vol.length   ? vol   : null;
  data.certificates = certs.length ? certs : null;

  return data;
}

// ── Generate ─────────────────────────────────────────────────────
async function generateResume() {
  const btn = document.getElementById('generate-btn');
  btn.disabled = true;
  btn.textContent = 'Generating…';
  document.getElementById('loader').style.display = 'flex';

  try {
    const res  = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(collectFormData()),
    });
    const data = await res.json();

    if (data.success) {
      showResult(data.pdf, data.tex);
      toast('Resume generated!', 'success');
    } else {
      toast('Error: ' + data.error, 'error');
      if (data.tex) showResult(null, data.tex);
    }
  } catch (e) {
    toast('Network error: ' + e.message, 'error');
  } finally {
    btn.disabled = false;
    btn.textContent = 'Generate Resume';
    document.getElementById('loader').style.display = 'none';
  }
}

function showResult(pdfBase64, texSource) {
  const section = document.getElementById('results');
  section.style.display = 'block';
  section.scrollIntoView({ behavior: 'smooth', block: 'start' });

  if (texSource) document.getElementById('tex-source').value = texSource;

  const container = document.getElementById('pdf-container');
  if (pdfBase64) {
    const blob = b64toBlob(pdfBase64, 'application/pdf');
    window._pdfBlob = blob;
    document.getElementById('pdf-iframe').src = URL.createObjectURL(blob);
    container.style.display = 'block';
  } else {
    container.style.display = 'none';
  }
}

function downloadPDF() {
  if (!window._pdfBlob) { toast('No PDF available', 'error'); return; }
  const url = URL.createObjectURL(window._pdfBlob);
  Object.assign(document.createElement('a'), { href: url, download: 'resume.pdf' }).click();
  URL.revokeObjectURL(url);
}

function b64toBlob(b64, type) {
  const raw = atob(b64);
  const arr = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) arr[i] = raw.charCodeAt(i);
  return new Blob([arr], { type });
}

// ── AI helpers ───────────────────────────────────────────────────
function extractText(r) {
  if (!r) return '';
  if (typeof r === 'string') return r;
  if (r.message?.content) {
    const c = r.message.content;
    if (typeof c === 'string') return c;
    if (Array.isArray(c)) return c.map(x => x.text ?? '').join('');
  }
  return String(r);
}

async function runAI(prompt, targetEl, btn, label) {
  if (typeof puter === 'undefined') { toast('AI unavailable (check network)', 'error'); return; }
  const original = targetEl.value;
  targetEl.value = 'Optimizing…';
  btn.disabled = true; btn.textContent = 'Optimizing…';
  try {
    targetEl.value = extractText(await puter.ai.chat(prompt));
    toast('Description updated!', 'success');
  } catch (e) {
    targetEl.value = original;
    toast('AI error: ' + e.message, 'error');
  } finally {
    btn.disabled = false; btn.textContent = label;
  }
}

const AI_SYSTEM = `You are a resume writing expert. Rewrite the given description to be concise, ATS-optimized, and impactful (minimum 3 lines). Return ONLY the rewritten description text — no headers, no labels, no markdown, no preamble.`;

function optimizeExp(id, btn) {
  const entry   = document.getElementById(`experience-entry-${id}`);
  const company = entry.querySelector('[data-field="company"]').value;
  const descEl  = entry.querySelector('[data-field="detail_description"]');
  runAI(`${AI_SYSTEM}\n\nCompany: ${company}\nOriginal: ${descEl.value}`, descEl, btn, 'Optimize with AI');
}

function optimizeProj(id, btn) {
  const entry  = document.getElementById(`projects-entry-${id}`);
  const title  = entry.querySelector('[data-field="title"]').value;
  const descEl = entry.querySelector('[data-field="description"]');
  runAI(`${AI_SYSTEM}\n\nProject: ${title}\nOriginal: ${descEl.value}`, descEl, btn, 'Optimize with AI');
}

function optimizePub(id, btn) {
  const entry  = document.getElementById(`publications-entry-${id}`);
  const title  = entry.querySelector('[data-field="title"]').value;
  const descEl = entry.querySelector('[data-field="description"]');
  runAI(`${AI_SYSTEM}\n\nPublication: ${title}\nOriginal: ${descEl.value}`, descEl, btn, 'Optimize with AI');
}

async function categorizeSkills() {
  if (typeof puter === 'undefined') { toast('AI unavailable (check network)', 'error'); return; }
  const raw = document.getElementById('raw-skills').value.trim();
  if (!raw) { toast('Enter some skills first', 'error'); return; }

  const btn = document.getElementById('ai-categorize-btn');
  btn.disabled = true; btn.textContent = 'Categorizing…';

  try {
    const text = extractText(await puter.ai.chat(
      `Categorize these skills into exactly these JSON keys: Languages, Frameworks, Tools, Platforms, Soft Skills, Others. Return ONLY valid JSON, no markdown.\nSkills: ${raw}`
    ));
    const cleaned = text.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
    const data = JSON.parse(cleaned);
    ['Languages', 'Frameworks', 'Tools', 'Platforms', 'Soft Skills', 'Others'].forEach(cat => {
      const el = document.getElementById('skills-' + cat.replace(' ', '-'));
      if (el && data[cat]) el.value = Array.isArray(data[cat]) ? data[cat].join(', ') : data[cat];
    });
    toast('Skills categorized!', 'success');
  } catch (e) {
    toast('AI error: ' + e.message, 'error');
  } finally {
    btn.disabled = false; btn.textContent = 'AI Categorize';
  }
}

// ── Toast ─────────────────────────────────────────────────────────
function toast(msg, type = 'info') {
  const el = document.createElement('div');
  el.className = `toast toast-${type}`;
  el.textContent = msg;
  document.getElementById('toast-container').appendChild(el);
  requestAnimationFrame(() => el.classList.add('show'));
  setTimeout(() => { el.classList.remove('show'); setTimeout(() => el.remove(), 300); }, 3500);
}

// ── Active nav on scroll ─────────────────────────────────────────
function syncNav() {
  const y = window.scrollY + 90;
  document.querySelectorAll('.card[id]').forEach(sec => {
    const link = document.querySelector(`.nav-link[href="#${sec.id}"]`);
    if (!link) return;
    const inView = y >= sec.offsetTop && y < sec.offsetTop + sec.offsetHeight;
    link.classList.toggle('active', inView);
  });
}

// ── Init ──────────────────────────────────────────────────────────
window.addEventListener('DOMContentLoaded', () => {
  ['education', 'experience', 'projects', 'publications', 'honors', 'volunteer', 'certificates']
    .forEach(addEntry);

  document.querySelectorAll('.nav-link').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      document.querySelector(a.getAttribute('href'))?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  window.addEventListener('scroll', syncNav, { passive: true });
});
