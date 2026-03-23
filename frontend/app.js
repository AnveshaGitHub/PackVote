const API = 'http://127.0.0.1:5000/api';

const DEST_IMAGES = {
  'Mumbai':      'https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&q=80',
  'Delhi':       'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&q=80',
  'Jaipur':      'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800&q=80',
  'Goa':         'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1600&q=80',
  'Kerala':      'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800&q=80',
  'Manali':      'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80',
  'Agra':        'https://images.unsplash.com/photo-1548013146-72479768bada?w=800&q=80',
  'Varanasi':    'https://images.unsplash.com/photo-1561361058-c24e01c78e6e?w=800&q=80',
  'Udaipur':     'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&q=80',
  'Mysuru':      'https://images.unsplash.com/photo-1580181591840-b5f3f9b27d16?w=800&q=80',
  'Rishikesh':   'https://images.unsplash.com/photo-1600697395543-31e0c3a25dbd?w=800&q=80',
  'Leh Ladakh':  'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
  'Shimla':      'https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&q=80',
  'Hampi':       'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&q=80',
  'Darjeeling':  'https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&q=80',
  'Pondicherry': 'https://images.unsplash.com/photo-1617469767053-d3b523a0b982?w=800&q=80',
  'Srinagar':    'https://images.unsplash.com/photo-1602532305019-3dbbd482dae7?w=800&q=80',
  'Coorg':       'https://images.unsplash.com/photo-1582053433976-25c00369831c?w=800&q=80',
  'Jaisalmer':   'https://images.unsplash.com/photo-1612214248522-5c09f1be0a2e?w=800&q=80',
  'Alleppey':    'https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=800&q=80',
  'Paris':       'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80',
  'Tokyo':       'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80',
  'Bali':        'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80',
  'Bangkok':     'https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=800&q=80',
  'Dubai':       'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80',
  'Singapore':   'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800&q=80',
  'Maldives':    'https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800&q=80',
  'London':      'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800&q=80',
  'Nepal':       'https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&q=80',
  'Sri Lanka':   'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&q=80',
  'default':     'https://images.unsplash.com/photo-1488085061387-422e29b40080?w=800&q=80'
};

const DEST_DESCS = {
  'Jaipur':     'The Pink City — palaces, forts and vibrant bazaars',
  'Goa':        "India's beach paradise — sun, seafood and parties",
  'Kerala':     'Backwaters, tea gardens and Ayurvedic retreats',
  'Manali':     'Adventure capital — skiing, trekking and mountain passes',
  'Varanasi':   'Oldest living city — ghats, rituals and spiritual energy',
  'Udaipur':    'City of lakes — the most romantic city in India',
  'Leh Ladakh': 'Roof of the world — monasteries and mountain passes',
  'Rishikesh':  'Yoga capital — river rafting and Ganges ghats',
  'Srinagar':   'Paradise on earth — Dal Lake houseboats and gardens',
  'Delhi':      "India's capital — Mughal monuments and chaotic bazaars",
  'Mumbai':     'City of dreams — Bollywood, street food and the sea',
  'Agra':       'Home of the Taj Mahal — Mughal architecture at its finest',
  'Hampi':      'UNESCO ruins of the Vijayanagara Empire amid boulders',
  'Coorg':      'Scotland of India — coffee estates and misty hills',
  'Jaisalmer':  'Golden city rising from the Thar Desert',
  'Paris':      'City of lights, art and cuisine',
  'Tokyo':      'Ultra-modern meets ancient tradition',
  'Bali':       'Tropical paradise with rich spiritual culture',
  'Dubai':      'City of superlatives — tallest, largest, most luxurious',
  'Maldives':   'Paradise overwater bungalows and crystal seas',
};

const DEST_COORDS = {
  'Jaipur':     [26.9124, 75.7873],
  'Goa':        [15.2993, 74.1240],
  'Kerala':     [10.8505, 76.2711],
  'Mumbai':     [19.0760, 72.8777],
  'Delhi':      [28.7041, 77.1025],
  'Manali':     [32.2396, 77.1887],
  'Agra':       [27.1767, 78.0081],
  'Varanasi':   [25.3176, 82.9739],
  'Udaipur':    [24.5854, 73.7125],
  'Leh Ladakh': [34.1526, 77.5770],
  'Rishikesh':  [30.0869, 78.2676],
  'Srinagar':   [34.0837, 74.7973],
  'Shimla':     [31.1048, 77.1734],
  'Darjeeling': [27.0360, 88.2627],
  'Hampi':      [15.3350, 76.4600],
  'Coorg':      [12.3375, 75.8069],
  'Jaisalmer':  [26.9157, 70.9083],
  'Mysuru':     [12.2958, 76.6394],
  'Paris':      [48.8566,  2.3522],
  'Tokyo':      [35.6762, 139.6503],
  'Bali':       [-8.3405, 115.0920],
  'Dubai':      [25.2048,  55.2708],
  'London':     [51.5074,  -0.1278],
  'Singapore':  [ 1.3521, 103.8198],
  'Maldives':   [ 3.2028,  73.2207],
  'Bangkok':    [13.7563, 100.5018],
};

// ── Utilities ─────────────────────────────────────────────────────────────
function getDestImage(name)  { return DEST_IMAGES[name] || DEST_IMAGES['default']; }
function getDestDesc(name)   { return DEST_DESCS[name]  || 'An incredible destination awaits!'; }
function getDestCoords(name) { return DEST_COORDS[name] || [20.5937, 78.9629]; }
function capitalize(s)       { return s ? s.charAt(0).toUpperCase() + s.slice(1) : '—'; }
function setText(id, val)    { const el = document.getElementById(id); if (el) el.textContent = val; }
function saveData(key, val)  { localStorage.setItem(key, JSON.stringify(val)); }
function loadData(key)       { try { return JSON.parse(localStorage.getItem(key)); } catch { return null; } }

// ── Toast ─────────────────────────────────────────────────────────────────
function showToast(message, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${type === 'success' ? '✅' : '❌'}</span> ${message}`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.animation = 'slideOut 0.3s ease forwards';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// ── Auth ──────────────────────────────────────────────────────────────────
function requireAuth() {
  const user = loadData('triply_user') || loadData('PackVote_user');
  if (!user) { window.location.href = 'login.html'; return null; }
  return user;
}

function loadUser() {
  return loadData('triply_user') || loadData('PackVote_user');
}

function saveUser(user) {
  localStorage.setItem('triply_user', JSON.stringify(user));
  localStorage.setItem('PackVote_user', JSON.stringify(user));
}

function logout() {
  localStorage.removeItem('triply_user');
  localStorage.removeItem('triply_group_id');
  localStorage.removeItem('triply_voter_name');
  localStorage.removeItem('triply_group_name');
  showToast('Logged out 👋');
  setTimeout(() => window.location.href = 'login.html', 800);
}

// ══════════════════════════════════════════════════════════════════════════
// INDEX PAGE
// ══════════════════════════════════════════════════════════════════════════
let members = [];

function addMember() {
  const input = document.getElementById('memberInput');
  if (!input) return;
  const name = input.value.trim();
  if (!name)               { showToast('Please enter a name', 'error'); return; }
  if (members.includes(name)) { showToast('Already added!', 'error'); return; }
  members.push(name);
  input.value = '';
  renderMembers();
  showToast(`${name} added! ✅`);
}

function renderMembers() {
  const list = document.getElementById('membersList');
  if (!list) return;
  list.innerHTML = members.map(m => `
    <div class="member-chip">
      <div class="member-avatar">${m[0].toUpperCase()}</div>
      ${m}
      <span class="member-remove" onclick="removeMember('${m}')">✕</span>
    </div>`).join('');
}

function removeMember(name) {
  members = members.filter(m => m !== name);
  renderMembers();
}

async function createGroup() {
  const user      = loadData('triply_user');
  const groupName = document.getElementById('groupName')?.value.trim();
  if (!groupName)         { showToast('Enter a group name', 'error'); return; }
  if (members.length < 1) { showToast('Add at least 1 member', 'error'); return; }
  try {
    const res  = await fetch(`${API}/group/create`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_name: groupName, members, user_id: user?.user_id || '' })
    });
    const data = await res.json();
    if (data.success) {
      saveData('triply_group_id',   data.group_id);
      saveData('triply_group_name', data.group_name);
      if (user) {
        if (!user.groups) user.groups = [];
        user.groups.push({ group_id: data.group_id, group_name: data.group_name, joined_at: new Date().toISOString() });
        saveData('triply_user', user);
      }
      showToast(`"${groupName}" created! 🎉`);
      setTimeout(() => window.location.href = 'vote.html', 1200);
    }
  } catch(e) { showToast('Cannot connect to server. Is Flask running?', 'error'); }
}

// ══════════════════════════════════════════════════════════════════════════
// VOTE PAGE
// ══════════════════════════════════════════════════════════════════════════
// VOTE_DESTINATIONS now managed dynamically — see initVotePage()

let currentCardIndex  = 0;
let votedDestinations = [];
let selectedBudget    = 'medium';
let selectedDuration  = 7;
let selectedStyles    = [];

let VOTE_DESTINATIONS = [];

const DEFAULT_DESTINATIONS = [
  { name: 'Jaipur',     desc: 'The Pink City — palaces, forts and vibrant bazaars',       tags: ['history','culture','food','shopping'], cost: '₹3,500/day' },
  { name: 'Goa',        desc: "India's beach paradise — sun, seafood and parties",        tags: ['beach','nightlife','food','adventure'], cost: '₹5,000/day' },
  { name: 'Kerala',     desc: 'Backwaters, tea gardens and Ayurvedic retreats',            tags: ['nature','wellness','romance','culture'],cost: '₹4,000/day' },
  { name: 'Manali',     desc: 'Adventure capital — skiing, trekking and Rohtang Pass',    tags: ['adventure','nature','romance'],         cost: '₹4,500/day' },
  { name: 'Varanasi',   desc: 'Oldest living city — ghats, rituals and spiritual energy', tags: ['culture','history','wellness'],         cost: '₹2,500/day' },
  { name: 'Leh Ladakh', desc: 'Roof of the world — monasteries and mountain passes',      tags: ['adventure','nature','culture'],         cost: '₹4,500/day' },
  { name: 'Udaipur',    desc: 'City of lakes — the most romantic city in India',          tags: ['romance','history','culture','art'],    cost: '₹4,000/day' },
  { name: 'Rishikesh',  desc: 'Yoga capital — river rafting and Ganges ghats',            tags: ['wellness','adventure','culture'],       cost: '₹2,500/day' },
  { name: 'Hampi',      desc: 'UNESCO ruins of the Vijayanagara Empire amid boulders',    tags: ['history','culture','adventure','art'],  cost: '₹2,000/day' },
  { name: 'Srinagar',   desc: 'Paradise on earth — Dal Lake houseboats and gardens',      tags: ['romance','nature','culture','history'], cost: '₹4,500/day' },
  { name: 'Coorg',      desc: 'Scotland of India — coffee estates and misty hills',       tags: ['nature','adventure','wellness'],        cost: '₹3,500/day' },
  { name: 'Jaisalmer',  desc: 'Golden city rising from the Thar Desert',                  tags: ['history','adventure','culture'],        cost: '₹3,000/day' },
];

function getDestTags(name) {
  const tagMap = {
    'Jaipur':['history','culture','food','shopping'],'Goa':['beach','nightlife','food','adventure'],
    'Kerala':['nature','wellness','romance','culture'],'Manali':['adventure','nature','romance'],
    'Varanasi':['culture','history','wellness'],'Leh Ladakh':['adventure','nature','culture'],
    'Udaipur':['romance','history','culture','art'],'Rishikesh':['wellness','adventure','culture'],
    'Hampi':['history','culture','adventure','art'],'Srinagar':['romance','nature','culture','history'],
    'Coorg':['nature','adventure','wellness'],'Jaisalmer':['history','adventure','culture'],
  };
  return tagMap[name] || ['travel','explore','adventure'];
}

function getDestCost(name) {
  const costMap = {
    'Jaipur':'₹3,500/day','Goa':'₹5,000/day','Kerala':'₹4,000/day','Manali':'₹4,500/day',
    'Varanasi':'₹2,500/day','Leh Ladakh':'₹4,500/day','Udaipur':'₹4,000/day',
    'Rishikesh':'₹2,500/day','Hampi':'₹2,000/day','Srinagar':'₹4,500/day',
    'Coorg':'₹3,500/day','Jaisalmer':'₹3,000/day',
  };
  return costMap[name] || '₹3,000/day';
}

async function initVotePage() {
  if (!document.getElementById('cardStack')) return;
  const savedUser  = loadData('triply_user');
  const groupId    = localStorage.getItem('PackVote_group_id') ||
                     localStorage.getItem('triply_group_id')   ||
                     loadData('triply_group_id');
  const groupEl = document.getElementById('groupId');
  const nameEl  = document.getElementById('voterName');
  if (groupId  && groupEl) groupEl.value = groupId;
  if (savedUser && nameEl) nameEl.value  = savedUser.name || '';
  if (groupId) {
    await loadGroupDestinations(groupId);
  } else {
    VOTE_DESTINATIONS = DEFAULT_DESTINATIONS;
    renderCards();
  }
}

async function loadGroupDestinations(groupId) {
  try {
    const res  = await fetch(`${API}/group/${groupId}/destinations`);
    const data = await res.json();
    const db   = data.destinations || [];
    if (db.length >= 2) {
      VOTE_DESTINATIONS = db.map(d => ({
        name: d.name,
        desc: getDestDesc(d.name) || `Explore the beauty of ${d.name}`,
        tags: getDestTags(d.name),
        cost: getDestCost(d.name)
      }));
      showToast(`${VOTE_DESTINATIONS.length} destinations loaded!`);
    } else {
      VOTE_DESTINATIONS = DEFAULT_DESTINATIONS;
    }
  } catch(e) {
    VOTE_DESTINATIONS = DEFAULT_DESTINATIONS;
  }
  renderCards();
}

function renderCards() {
  const stack = document.getElementById('cardStack');
  if (!stack) return;
  stack.innerHTML = '';
  const remaining = VOTE_DESTINATIONS.slice(currentCardIndex, currentCardIndex + 3);
  if (remaining.length === 0) { showDoneState(); return; }
  [...remaining].reverse().forEach((dest, i) => {
    const isTop = i === remaining.length - 1;
    const card  = document.createElement('div');
    card.className = 'v-card';
    card.innerHTML = `
      <div class="like-stamp">LOVE IT ♥</div>
      <div class="nope-stamp">NOPE ✕</div>
      <img src="${getDestImage(dest.name)}" alt="${dest.name}" draggable="false"/>
      <div class="v-card-body">
        <div>
          <div class="v-card-title">${dest.name}</div>
          <div class="v-card-desc">${dest.desc}</div>
          <div class="v-card-tags">
            ${dest.tags.map(t => `<span class="v-card-tag">${t}</span>`).join('')}
          </div>
        </div>
        <div class="v-card-cost">💰 ${dest.cost}</div>
      </div>`;
    stack.appendChild(card);
    if (isTop) initDrag(card);
  });
  updateProgress();
}

function initDrag(card) {
  let startX = 0, currentX = 0, isDragging = false;
  card.addEventListener('mousedown', e => { isDragging = true; startX = e.clientX; card.style.transition = 'none'; });
  document.addEventListener('mousemove', e => {
    if (!isDragging) return;
    currentX = e.clientX - startX;
    card.style.transform = `translateX(${currentX}px) rotate(${currentX * 0.04}deg)`;
    const like = card.querySelector('.like-stamp');
    const nope = card.querySelector('.nope-stamp');
    if (like) like.style.opacity = currentX > 40 ? Math.min((currentX-40)/80, 1) : 0;
    if (nope) nope.style.opacity = currentX < -40 ? Math.min((-currentX-40)/80, 1) : 0;
  });
  document.addEventListener('mouseup', () => {
    if (!isDragging) return;
    isDragging = false;
    if      (currentX >  90) animateCard(card, 'love');
    else if (currentX < -90) animateCard(card, 'skip');
    else { card.style.transition = 'transform 0.4s ease'; card.style.transform = ''; }
    currentX = 0;
  });
  card.addEventListener('touchstart', e => { startX = e.touches[0].clientX; card.style.transition = 'none'; });
  card.addEventListener('touchmove',  e => {
    currentX = e.touches[0].clientX - startX;
    card.style.transform = `translateX(${currentX}px) rotate(${currentX * 0.04}deg)`;
    const like = card.querySelector('.like-stamp');
    const nope = card.querySelector('.nope-stamp');
    if (like) like.style.opacity = currentX > 40 ? Math.min((currentX-40)/80, 1) : 0;
    if (nope) nope.style.opacity = currentX < -40 ? Math.min((-currentX-40)/80, 1) : 0;
  });
  card.addEventListener('touchend', () => {
    if      (currentX >  90) animateCard(card, 'love');
    else if (currentX < -90) animateCard(card, 'skip');
    else { card.style.transition = 'transform 0.4s ease'; card.style.transform = ''; }
    currentX = 0;
  });
}

function animateCard(card, direction) {
  const dest = VOTE_DESTINATIONS[currentCardIndex];
  card.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
  card.style.transform  = `translateX(${direction === 'love' ? 900 : -900}px) rotate(${direction === 'love' ? 25 : -25}deg)`;
  card.style.opacity    = '0';
  if (direction === 'love' || direction === 'maybe') {
    votedDestinations.push(dest.name);
    showToast(direction === 'love' ? `❤️ ${dest.name} added!` : `⭐ ${dest.name} maybe!`);
  }
  currentCardIndex++;
  setTimeout(renderCards, 380);
}

function swipeCard(direction) {
  const stack   = document.getElementById('cardStack');
  if (!stack) return;
  const topCard = stack.lastElementChild;
  if (topCard && topCard.classList.contains('v-card')) animateCard(topCard, direction);
  else showDoneState();
}

function updateProgress() {
  const pct     = Math.round((currentCardIndex / VOTE_DESTINATIONS.length) * 100);
  const fill    = document.getElementById('progressFill');
  const counter = document.getElementById('voteCounter');
  if (fill)    fill.style.width    = pct + '%';
  if (counter) counter.textContent = `${currentCardIndex} / ${VOTE_DESTINATIONS.length} voted`;
}

function showDoneState() {
  const stack   = document.getElementById('cardStack');
  const done    = document.getElementById('doneState');
  const actions = document.getElementById('voteActionsRow');
  if (stack)   stack.style.display   = 'none';
  if (done)    done.style.display    = 'block';
  if (actions) actions.style.display = 'none';
  updateProgress();
}

function selectBudget(el) {
  document.querySelectorAll('#budgetTags .tag').forEach(t => t.classList.remove('selected'));
  el.classList.add('selected');
  selectedBudget = el.dataset.value;
}

function toggleStyle(el) {
  el.classList.toggle('selected');
  const raw   = el.textContent.replace(/[^\w\s]/g,'').trim().toLowerCase();
  const label = raw.split(' ').pop();
  if (el.classList.contains('selected')) selectedStyles.push(label);
  else selectedStyles = selectedStyles.filter(s => s !== label);
}

async function submitVote() {
  const voterName = document.getElementById('voterName')?.value.trim();
  const groupId   = document.getElementById('groupId')?.value.trim() || loadData('triply_group_id');
  const duration  = parseInt(document.getElementById('duration')?.value || '7');
  const month     = document.getElementById('month')?.value || 'December';
  if (!voterName) { showToast('Enter your name', 'error'); return; }
  if (!groupId)   { showToast('Enter a Group ID', 'error'); return; }
  const preferences = {
    destinations:  votedDestinations.length > 0 ? votedDestinations : ['Jaipur','Goa','Kerala'],
    budget:        selectedBudget,
    travel_style:  selectedStyles.length > 0 ? selectedStyles : ['culture','food'],
    duration, month
  };
  try {
    const res  = await fetch(`${API}/vote/submit`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_id: groupId, user_name: voterName, preferences })
    });
    const data = await res.json();
    if (data.success) {
      saveData('triply_group_id',   groupId);
      saveData('triply_voter_name', voterName);
      showToast('Vote submitted! 🎉');
      setTimeout(() => window.location.href = 'results.html', 1200);
    } else {
      showToast(data.error || 'Error submitting vote', 'error');
    }
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

// ══════════════════════════════════════════════════════════════════════════
// RESULTS PAGE
// ══════════════════════════════════════════════════════════════════════════
let triplyMap = null;

async function initResultsPage() {
  if (!document.getElementById('winnerName')) return;
  const user = loadData('triply_user');
  if (!user) { loadDemoResults(); return; }

  const groupId = localStorage.getItem('PackVote_group_id') ||
                  localStorage.getItem('triply_group_id') ||
                  loadData('triply_group_id');

  if (!groupId) {
    loadDemoResults();
    return;
  }
  await loadRealResults(groupId);
}

async function loadRealResults(groupId) {
  try {
    const res  = await fetch(`${API}/vote/results/${groupId}`);
    const data = await res.json();
    if (data.error || !data.consensus || !data.consensus.winner) {
      showToast('No votes found yet — showing demo', 'error');
      loadDemoResults();
      return;
    }
    renderResults(data);
    const winner = data.consensus.winner;
    console.log('Winner:', winner);
    await loadWeather(winner);
    await loadItinerary(winner, data.consensus);
    await loadDeepLinks(
      winner,
      data.consensus.avg_duration    || 7,
      data.consensus.consensus_budget || 'medium'
    );
  } catch(e) {
    console.error('loadRealResults error:', e);
    loadDemoResults();
  }
}

function loadDemoResults() {
  renderResults({
    group_name: 'Demo Group', total_votes: 3,
    consensus: {
      winner: 'Jaipur',
      top_destinations: [
        { destination: 'Jaipur',  percentage: 100 },
        { destination: 'Goa',     percentage: 78  },
        { destination: 'Kerala',  percentage: 65  },
        { destination: 'Manali',  percentage: 50  },
        { destination: 'Udaipur', percentage: 40  },
      ],
      consensus_budget: 'medium', avg_duration: 7,
      consensus_month: 'December',
      top_styles: ['culture','food','adventure'], conflicts: []
    },
    recommendations: [
      { destination: 'Jaipur',  match_percentage: 95, description: 'The Pink City',  avg_cost_per_day: 3500, tags: ['history','culture'] },
      { destination: 'Udaipur', match_percentage: 88, description: 'City of Lakes',  avg_cost_per_day: 4000, tags: ['romance','history'] },
      { destination: 'Jodhpur', match_percentage: 82, description: 'The Blue City',  avg_cost_per_day: 3000, tags: ['history','culture'] },
    ]
  });
  loadWeather('Jaipur');
  loadItinerary('Jaipur', { avg_duration:7, consensus_budget:'medium', top_styles:['culture'], consensus_month:'December' });
}

function renderResults(data) {
  const c = data.consensus;
  setText('winnerName', c.winner || 'Your Destination');
  setText('winnerDesc', getDestDesc(c.winner));
  const bgImg = document.getElementById('winnerBgImg');
  if (bgImg) {
    bgImg.style.opacity = '0';
    bgImg.src = getDestImage(c.winner);
    bgImg.onload = () => {
      bgImg.style.transition = 'opacity 1.5s ease';
      bgImg.style.opacity    = '1';
    };
  }
  setText('statVoters', data.total_votes);
  setText('statDays',   (c.avg_duration||'—') + (c.avg_duration ? 'd' : ''));
  setText('statBudget', capitalize(c.consensus_budget));
  setText('statMonth',  c.consensus_month?.slice(0,3) || '—');

  const scoreList = document.getElementById('scoreList');
  if (scoreList && c.top_destinations) {
    scoreList.innerHTML = c.top_destinations.map((d,i) => `
      <div class="score-bar">
        <div class="score-label">${i===0?'🏆':'#'+(i+1)} ${d.destination}</div>
        <div class="score-track"><div class="score-fill" style="width:0%" data-pct="${d.percentage}"></div></div>
        <div class="score-pct">${d.percentage}%</div>
      </div>`).join('');
    setTimeout(() => {
      document.querySelectorAll('.score-fill').forEach(el => { el.style.width = el.dataset.pct + '%'; });
    }, 400);
  }

  const recList = document.getElementById('recList');
  if (recList && data.recommendations) {
    recList.innerHTML = data.recommendations.map((r,i) => `
      <div class="rec-card">
        <div class="rec-rank ${i===0?'top':''}">${i===0?'🥇':i===1?'🥈':'🥉'}</div>
        <img src="${getDestImage(r.destination)}"
             style="width:56px;height:56px;border-radius:10px;object-fit:cover;flex-shrink:0;"
             alt="${r.destination}"/>
        <div class="rec-info">
          <div class="rec-name">${r.destination}</div>
          <div class="rec-desc">${r.description}</div>
          <div class="rec-meta">
            <span>₹${(r.avg_cost_per_day||0).toLocaleString()}/day</span>
            <span>${(r.tags||[]).slice(0,2).join(' · ')}</span>
          </div>
        </div>
        <div class="rec-match">${r.match_percentage}%</div>
      </div>`).join('');
  }

  if (c.conflicts?.length > 0) {
    const section = document.getElementById('conflictSection');
    const list    = document.getElementById('conflictList');
    if (section) section.style.display = 'block';
    if (list) list.innerHTML = c.conflicts.map(cf => `
      <div class="conflict-alert">
        <span class="conflict-icon">${cf.severity==='high'?'🔴':'🟡'}</span>
        <span class="conflict-text">${cf.message}</span>
      </div>`).join('');
  }
  initMap(c.winner);
}

async function loadWeather(destination) {
  try {
    const res  = await fetch(`${API}/weather/${encodeURIComponent(destination)}`);
    const data = await res.json();
    setText('weatherTemp',     `${data.temperature_c}°C`);
    setText('weatherDesc',     data.description || 'Clear skies');
    setText('weatherHumidity', `Humidity: ${data.humidity}%`);
    const forecastRow = document.getElementById('forecastRow');
    if (forecastRow && data.forecast?.length > 0) {
      forecastRow.innerHTML = data.forecast.map(f => `
        <div class="forecast-day">
          <div class="date">${f.date}</div>
          <div class="temp">${f.max_temp}° / ${f.min_temp}°</div>
          <div style="font-size:0.72rem;color:var(--text-muted);margin-top:2px;">
            ${(f.description||'').split(' ').slice(0,2).join(' ')}
          </div>
        </div>`).join('');
    }
  } catch(e) { setText('weatherDesc', 'Weather data unavailable'); }
}

async function loadItinerary(destination, consensus) {
  const itinDiv = document.getElementById('itineraryList');
  if (itinDiv) itinDiv.innerHTML = `
    <div style="text-align:center;padding:48px;color:var(--text-muted);">
      <div style="font-size:2rem;margin-bottom:12px;">🤖</div>
      <div style="font-weight:700;margin-bottom:6px;">Building your AI itinerary...</div>
      <div style="font-size:0.85rem;">Fetching real data for ${destination}</div>
    </div>`;

  const groupId = localStorage.getItem('PackVote_group_id') ||
                  localStorage.getItem('triply_group_id') ||
                  loadData('triply_group_id');

  // Step 1 — Check if notebook already saved an itinerary
  if (groupId) {
    try {
      const res  = await fetch(`${API}/itinerary/group/${groupId}`);
      const data = await res.json();
      if (data.success && data.itinerary) {
        renderCost(buildCostFromItinerary(data.itinerary));
        renderAIItinerary(data.itinerary);
        return;
      }
    } catch(e) {}
  }

  // Step 2 — Generate live via Groq AI
  try {
    const res  = await fetch(`${API}/itinerary/ai-generate`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        destination,
        duration:     consensus.avg_duration     || 5,
        budget:       consensus.consensus_budget || 'medium',
        travel_style: consensus.top_styles       || ['culture'],
        month:        consensus.consensus_month  || 'December',
        group_size:   consensus.total_voters     || 4,
        food_pref:    'both',
        group_type:   'friends'
      })
    });
    const data = await res.json();
    if (data.success && data.itinerary) {
      renderCost(buildCostFromItinerary(data.itinerary));
      renderAIItinerary(data.itinerary);
      return;
    }
  } catch(e) {
    console.log('AI itinerary failed:', e);
  }

  // Step 3 — Final fallback
  renderFallbackItinerary(destination);
}

function buildCostFromItinerary(itinerary) {
  if (itinerary.total_cost) {
    return { per_person: { total: itinerary.total_cost.per_person_inr } };
  }
  if (itinerary.estimated_cost) return itinerary.estimated_cost;
  return null;
}

function renderAIItinerary(itinerary) {
  const list = document.getElementById('itineraryList');
  if (!list) return;
  const aiTag = itinerary.ai_powered
    ? `<span style="background:rgba(108,99,255,0.15);color:#a89bff;padding:3px 10px;border-radius:50px;font-size:0.72rem;font-weight:700;margin-left:8px;">✨ AI Generated</span>`
    : '';
  let html = `
    <div class="card" style="margin-bottom:20px;background:linear-gradient(135deg,rgba(108,99,255,0.08),rgba(255,101,132,0.05));">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
        <div style="font-size:1rem;font-weight:700;">${itinerary.destination||''}</div>${aiTag}
      </div>
      <div style="font-size:0.88rem;color:var(--text-secondary);font-style:italic;margin-bottom:12px;">"${itinerary.theme||''}"</div>
      ${(itinerary.highlights||[]).map(h=>`<div style="font-size:0.85rem;margin-bottom:4px;"><span style="color:var(--accent-3);">★</span> ${h}</div>`).join('')}
    </div>`;
  const reach = itinerary.reach || {};
  if (Object.keys(reach).length > 0) {
    html += `<div class="card" style="margin-bottom:16px;">
      <div style="font-weight:700;margin-bottom:10px;">🚂 How to reach ${itinerary.destination}</div>
      ${reach.by_train  ? `<p style="font-size:0.83rem;margin:4px 0;"><strong>🚆 Train:</strong> ${reach.by_train}</p>`  : ''}
      ${reach.by_bus    ? `<p style="font-size:0.83rem;margin:4px 0;"><strong>🚌 Bus:</strong> ${reach.by_bus}</p>`      : ''}
      ${reach.by_flight ? `<p style="font-size:0.83rem;margin:4px 0;"><strong>✈️ Flight:</strong> ${reach.by_flight}</p>`: ''}
      ${reach.by_road   ? `<p style="font-size:0.83rem;margin:4px 0;"><strong>🚗 Road:</strong> ${reach.by_road}</p>`   : ''}
    </div>`;
  }
  (itinerary.days||[]).forEach(day => {
    html += `
      <div class="day-card" style="margin-bottom:14px;">
        <div class="day-header" onclick="toggleDay(this)">
          <div class="day-number">D${day.day}</div>
          <div>
            <div class="day-title">${day.title||''}</div>
            <div style="font-size:0.78rem;color:var(--text-muted);">${day.day_cost_per_person||''} per person · ${day.local_transport||''}</div>
          </div>
          <span style="margin-left:auto;color:var(--text-muted);">▾</span>
        </div>
        <div class="day-body">
          ${renderSlot('🌅 Morning',   day.morning)}
          ${renderSlot('☀️ Afternoon', day.afternoon)}
          ${renderSlot('🌇 Evening',   day.evening)}
          ${renderMeal('🍽️ Lunch',  day.lunch)}
          ${renderMeal('🌙 Dinner', day.dinner)}
          ${day.pro_tip ? `<div style="background:rgba(255,215,0,0.08);border-radius:8px;padding:8px 12px;margin-top:8px;font-size:0.82rem;">💡 ${day.pro_tip}</div>` : ''}
        </div>
      </div>`;
  });
  if ((itinerary.must_eat||[]).length > 0) {
    html += `<div class="card" style="margin-bottom:14px;">
      <div style="font-weight:700;margin-bottom:10px;">🍜 Must-try food</div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;">
        ${itinerary.must_eat.map(f => {
          const dish  = typeof f==='string' ? f : f.dish||'';
          const where = typeof f==='object' ? (f.where||'') : '';
          const price = typeof f==='object' ? (f.price||'') : '';
          return `<div style="background:rgba(255,101,132,0.08);border:1px solid rgba(255,101,132,0.2);border-radius:8px;padding:6px 12px;font-size:0.8rem;">
            <div style="font-weight:700;">${dish}</div>
            ${where ? `<div style="color:var(--text-muted);font-size:0.72rem;">${where}${price?' · '+price:''}</div>` : ''}
          </div>`;
        }).join('')}
      </div>
    </div>`;
  }
  if ((itinerary.packing||[]).length > 0) {
    html += `<div class="card" style="margin-bottom:14px;">
      <div style="font-weight:700;margin-bottom:8px;">🎒 What to pack</div>
      ${itinerary.packing.map(p=>`<span style="display:inline-block;background:rgba(108,99,255,0.08);border-radius:50px;padding:4px 12px;margin:3px;font-size:0.8rem;">✓ ${p}</span>`).join('')}
    </div>`;
  }
  const cost = itinerary.total_cost;
  if (cost) {
    html += `<div class="card" style="background:linear-gradient(135deg,rgba(255,215,0,0.1),rgba(255,101,132,0.08));margin-bottom:14px;">
      <div style="font-weight:700;font-size:1.2rem;margin-bottom:4px;">💰 ${cost.per_person_inr||''} per person</div>
      <div style="font-size:0.85rem;color:var(--text-secondary);">${cost.for_group_inr||''} total for the group</div>
      ${cost.breakdown ? `<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;">
        ${Object.entries(cost.breakdown).map(([k,v])=>`<span style="background:var(--bg-card);border-radius:8px;padding:4px 10px;font-size:0.78rem;">${k}: <strong>${v}</strong></span>`).join('')}
      </div>` : ''}
    </div>`;
  }
  list.innerHTML = html;
}

function renderSlot(label, slot) {
  if (!slot) return '';
  return `<div style="border-left:3px solid rgba(108,99,255,0.3);padding:8px 12px;margin-bottom:8px;">
    <div style="font-size:0.72rem;color:var(--text-muted);font-weight:600;">${label}${slot.time?' · '+slot.time:''}</div>
    <div style="font-weight:700;font-size:0.9rem;">${slot.activity||''}</div>
    <div style="font-size:0.82rem;color:var(--text-secondary);margin-top:2px;">${slot.description||''}</div>
    <div style="font-size:0.75rem;margin-top:4px;display:flex;gap:12px;flex-wrap:wrap;">
      ${slot.cost      ? `<span style="color:var(--accent-gold);">💰 ${slot.cost}</span>`     : ''}
      ${slot.transport ? `<span style="color:var(--text-muted);">🚗 ${slot.transport}</span>` : ''}
      ${slot.tips      ? `<span style="color:var(--accent-3);">💡 ${slot.tips}</span>`         : ''}
    </div>
  </div>`;
}

function renderMeal(label, meal) {
  if (!meal) return '';
  const typeColor = meal.type==='veg' ? '#43e97b' : meal.type==='nonveg' ? '#ff6584' : '#ffd700';
  return `<div style="padding:8px 0;border-top:1px solid var(--border);">
    <div style="font-size:0.72rem;color:var(--text-muted);font-weight:600;">${label}</div>
    <div style="font-size:0.85rem;font-weight:700;">${meal.restaurant||''}${meal.area?' · '+meal.area:''}</div>
    <div style="font-size:0.75rem;display:flex;gap:10px;margin-top:3px;flex-wrap:wrap;">
      ${meal.type          ? `<span style="color:${typeColor};">● ${meal.type}</span>`             : ''}
      ${meal.cuisine       ? `<span style="color:var(--text-muted);">${meal.cuisine}</span>`       : ''}
      ${meal.must_try      ? `<span>Try: <strong>${meal.must_try}</strong></span>`                 : ''}
      ${meal.price_for_two ? `<span style="color:var(--accent-gold);">${meal.price_for_two}</span>`: ''}
    </div>
  </div>`;
}

async function loadDeepLinks(destination, duration, budget) {
  try {
    const res  = await fetch(`${API}/deeplinks`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ destination, duration, budget })
    });
    const data = await res.json();
    if (data.links) renderDeepLinks(data.links, destination);
  } catch(e) {
    console.log('Deep links unavailable:', e);
  }
}

function renderDeepLinks(links, destination) {
  const cats = {
    flights:    { el: 'linksFlights',    items: links.flights    || [] },
    trains:     { el: 'linksTrains',     items: links.trains     || [] },
    buses:      { el: 'linksBuses',      items: links.buses      || [] },
    hotels:     { el: 'linksHotels',     items: links.hotels     || [] },
    food:       { el: 'linksFood',       items: links.food       || [] },
    activities: { el: 'linksActivities', items: links.activities || [] },
  };
  for (const [cat, { el, items }] of Object.entries(cats)) {
    const container = document.getElementById(el);
    if (!container || items.length === 0) continue;
    container.innerHTML = items.map(link => `
      <a href="${link.url}" target="_blank" class="booking-btn">
        <span class="booking-btn-logo">${link.emoji||'🔗'}</span>
        <div class="booking-btn-info">
          <span class="booking-btn-name">${link.name}</span>
          <span class="booking-btn-note">${link.note||''}</span>
        </div>
      </a>`).join('');
  }
}

function renderCost(cost) {
  const grid = document.getElementById('costGrid');
  if (!grid || !cost?.per_person) return;
  const p = cost.per_person;
  grid.innerHTML = `
    <div class="cost-item"><div class="cost-item-label">✈️ Flights</div><div class="cost-item-value">₹${(p.flights||0).toLocaleString()}</div></div>
    <div class="cost-item"><div class="cost-item-label">🏨 Hotel</div><div class="cost-item-value">₹${(p.accommodation||0).toLocaleString()}</div></div>
    <div class="cost-item"><div class="cost-item-label">🍜 Food</div><div class="cost-item-value">₹${(p.food||0).toLocaleString()}</div></div>
    <div class="cost-item"><div class="cost-item-label">🎟️ Activities</div><div class="cost-item-value">₹${(p.activities||0).toLocaleString()}</div></div>
    <div class="cost-item" style="grid-column:span 2;border-color:rgba(255,215,0,0.3);">
      <div class="cost-item-label">💰 Total per person</div>
      <div class="cost-item-value" style="font-size:1.8rem;">₹${(p.total||0).toLocaleString()}</div>
    </div>`;
}

function renderItinerary(itinerary) {
  const list = document.getElementById('itineraryList');
  if (!list) return;
  const days = itinerary.days || [];
  if (days.length === 0) { renderFallbackItinerary(itinerary.destination); return; }
  list.innerHTML = days.map(day => `
    <div class="day-card">
      <div class="day-header" onclick="toggleDay(this)">
        <div class="day-number">D${day.day}</div>
        <div>
          <div class="day-title">${day.title}</div>
          <div style="font-size:0.8rem;color:var(--text-muted);">${(day.activities||[]).length} activities</div>
        </div>
        <span style="margin-left:auto;color:var(--text-muted);">▾</span>
      </div>
      <div class="day-body">
        ${(day.activities||[]).map(a => `
          <div class="activity">
            <div class="activity-dot"></div>
            <div>
              <div class="activity-name">${a.name||'Local Exploration'}</div>
              <div class="activity-type">${a.type||'experience'}${a.opening_hours?' · '+a.opening_hours:''}</div>
            </div>
          </div>`).join('')}
      </div>
    </div>`).join('');
}

function renderFallbackItinerary(destination) {
  renderItinerary({ destination, days: [
    { day:1, title:'Arrival & Exploration',  activities:[{name:'Check in & freshen up',type:'accommodation'},{name:'Evening walk',type:'sightseeing'},{name:'Welcome dinner',type:'food'}] },
    { day:2, title:'Main Attractions',       activities:[{name:'Top historical sites',type:'sightseeing'},{name:'Local market',type:'shopping'},{name:'Street food lunch',type:'food'}] },
    { day:3, title:'Culture & Heritage',     activities:[{name:'Museum visit',type:'culture'},{name:'Art gallery',type:'art'},{name:'Traditional dinner',type:'food'}] },
    { day:4, title:'Adventure Day',          activities:[{name:'Guided tour',type:'tour'},{name:'Adventure activity',type:'adventure'},{name:'Rooftop dinner',type:'food'}] },
    { day:5, title:'Leisure & Departure',    activities:[{name:'Morning at leisure',type:'relaxation'},{name:'Last minute shopping',type:'shopping'},{name:'Farewell dinner',type:'food'}] },
  ]});
}

function toggleDay(header) {
  header.classList.toggle('open');
  header.nextElementSibling.classList.toggle('open');
}

function initMap(destination) {
  if (!window.L) return;
  const mapEl = document.getElementById('map');
  if (!mapEl || triplyMap) return;
  const coords = getDestCoords(destination);
  triplyMap = L.map('map').setView(coords, 11);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(triplyMap);
  const icon = L.divIcon({
    html: `<div style="background:linear-gradient(135deg,#6c63ff,#ff6584);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 4px 16px rgba(108,99,255,0.5);border:3px solid white;">✈</div>`,
    className: '', iconSize: [40,40], iconAnchor: [20,20]
  });
  L.marker(coords, { icon }).addTo(triplyMap)
   .bindPopup(`<b>${destination}</b><br>Your group's destination! 🎉`).openPopup();
}

// ── Share ─────────────────────────────────────────────────────────────────
function shareWhatsApp() {
  const winner = document.getElementById('winnerName')?.textContent || 'our destination';
  window.open(`https://wa.me/?text=${encodeURIComponent(
    `🌍 Our group is going to *${winner}*!\nPlanned with PackVote ✈\nVote. Plan. Fly.`
  )}`, '_blank');
}
function copyLink() {
  navigator.clipboard.writeText(window.location.href);
  showToast('Link copied! 🔗');
}

// ══════════════════════════════════════════════════════════════════════════
// EXPENSES PAGE
// ══════════════════════════════════════════════════════════════════════════
let expGroupId   = '';
let expMembers   = [];
let selectedCat  = 'food';
let splitType    = 'equal';
let expenseChart = null;

function initExpensesPage() {
  if (!document.getElementById('expGroupId')) return;
  const savedGroup   = loadData('triply_group_id');
  if (savedGroup) {
    document.getElementById('expGroupId').value = savedGroup;
    const savedMembers = loadData('triply_exp_members_' + savedGroup);
    if (savedMembers && savedMembers.length >= 2) {
      expMembers = savedMembers;
      renderExpMembersList();
      setupGroupDirect(savedGroup, savedMembers);
    }
  }
}

function addExpMember() {
  const input = document.getElementById('expMemberInput');
  const name  = input.value.trim();
  if (!name)                     { showToast('Enter a name', 'error'); return; }
  if (expMembers.includes(name)) { showToast('Already added', 'error'); return; }
  expMembers.push(name);
  input.value = '';
  renderExpMembersList();
  showToast(`${name} added!`);
}

function renderExpMembersList() {
  const list = document.getElementById('expMembersList');
  if (!list) return;
  list.innerHTML = expMembers.map(m => `
    <div class="member-check checked">
      <div class="member-avatar" style="width:20px;height:20px;font-size:0.65rem;">${m[0].toUpperCase()}</div>
      ${m}
    </div>`).join('');
}

function setupGroup() {
  const groupId = document.getElementById('expGroupId').value.trim();
  if (!groupId)              { showToast('Enter a group ID', 'error'); return; }
  if (expMembers.length < 2) { showToast('Add at least 2 members', 'error'); return; }
  expGroupId   = '';
  expenseChart = null;
  ['chartCard','balancesCard','settlementsCard','shareCard'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.style.display = 'none';
  });
  setText('statTotal', '₹0'); setText('statPerPerson', '₹0');
  setText('statCount', '0');  setText('statSettlements', '0');
  setupGroupDirect(groupId, expMembers);
}

function setupGroupDirect(groupId, members) {
  expGroupId = groupId;
  expMembers = members;
  saveData('triply_exp_members_' + groupId, members);
  saveData('triply_group_id', groupId);
  const setupEl = document.getElementById('groupSetup');
  const formEl  = document.getElementById('addExpenseForm');
  const barEl   = document.getElementById('groupInfoBar');
  if (setupEl) setupEl.style.display   = 'none';
  if (formEl)  formEl.style.display    = 'block';
  if (barEl)   barEl.style.display     = 'flex';
  setText('activeGroupLabel',   groupId);
  setText('activeMembersLabel', members.join(', '));
  const select = document.getElementById('expPaidBy');
  if (select) {
    select.innerHTML = '<option value="">Select who paid</option>' +
      members.map(m => `<option value="${m}">${m}</option>`).join('');
  }
  renderSplitMembers(members);
  loadExpenses();
}

function switchGroup() {
  expGroupId = ''; expMembers = []; expenseChart = null;
  ['groupInfoBar','addExpenseForm','chartCard','balancesCard','settlementsCard','shareCard'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.style.display = 'none';
  });
  setText('statTotal','₹0'); setText('statPerPerson','₹0');
  setText('statCount','0');  setText('statSettlements','0');
  const expList = document.getElementById('expensesList');
  if (expList) expList.innerHTML = `<div class="empty-expenses"><span class="empty-emoji">🧾</span><p>Set up your group above to start tracking!</p></div>`;
  const membersListEl = document.getElementById('expMembersList');
  const groupIdEl     = document.getElementById('expGroupId');
  if (membersListEl) membersListEl.innerHTML = '';
  if (groupIdEl)     groupIdEl.value = '';
  const setupEl = document.getElementById('groupSetup');
  if (setupEl) setupEl.style.display = 'block';
  showToast('Switched! Enter new group details 🔄');
}

function renderSplitMembers(members) {
  const container = document.getElementById('splitMembers');
  if (!container) return;
  container.innerHTML = members.map(m => `
    <div class="member-check checked" onclick="toggleSplitMember(this)" data-member="${m}">
      <div class="member-avatar" style="width:20px;height:20px;font-size:0.65rem;">${m[0].toUpperCase()}</div>
      ${m}
    </div>`).join('');
}

function toggleSplitMember(el) {
  el.classList.toggle('checked');
  if (splitType === 'custom') renderCustomSplitInputs();
}

function selectCat(el) {
  document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  selectedCat = el.dataset.cat;
}

function setSplitType(type) {
  splitType = type;
  const equalEl  = document.getElementById('splitEqual');
  const customEl = document.getElementById('splitCustom');
  const areaEl   = document.getElementById('customSplitArea');
  if (equalEl)  equalEl.classList.toggle('selected',  type === 'equal');
  if (customEl) customEl.classList.toggle('selected', type === 'custom');
  if (areaEl)   areaEl.style.display = type === 'custom' ? 'block' : 'none';
  if (type === 'custom') renderCustomSplitInputs();
}

function renderCustomSplitInputs() {
  const checked   = [...document.querySelectorAll('#splitMembers .member-check.checked')];
  const amount    = parseFloat(document.getElementById('expAmount')?.value) || 0;
  const perPerson = checked.length > 0 ? (amount / checked.length).toFixed(2) : 0;
  const container = document.getElementById('customSplitInputs');
  if (!container) return;
  container.innerHTML = checked.map(el => {
    const member = el.dataset.member;
    return `<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
      <span style="min-width:100px;font-size:0.85rem;">${member}</span>
      <input type="number" class="form-input" id="custom_${member}" value="${perPerson}" step="0.01" min="0" style="flex:1;" placeholder="0.00"/>
    </div>`;
  }).join('');
}

async function submitExpense() {
  const desc    = document.getElementById('expDesc')?.value.trim();
  const amount  = parseFloat(document.getElementById('expAmount')?.value);
  const paidBy  = document.getElementById('expPaidBy')?.value;
  const checked = [...document.querySelectorAll('#splitMembers .member-check.checked')]
                    .map(el => el.dataset.member);
  if (!desc)                { showToast('Enter a description', 'error'); return; }
  if (!amount || amount<=0) { showToast('Enter a valid amount', 'error'); return; }
  if (!paidBy)              { showToast('Select who paid', 'error'); return; }
  if (checked.length === 0) { showToast('Select at least 1 member to split', 'error'); return; }
  let splitAmong = checked;
  if (splitType === 'custom') {
    const customSplits = {};
    let total = 0;
    for (const member of checked) {
      const val = parseFloat(document.getElementById(`custom_${member}`)?.value || 0);
      customSplits[member] = val;
      total += val;
    }
    if (Math.abs(total - amount) > 0.5) {
      showToast(`Custom split total (₹${total}) must equal amount (₹${amount})`, 'error');
      return;
    }
    splitAmong = customSplits;
  }
  try {
    const res  = await fetch(`${API}/expenses/add`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_id: expGroupId, paid_by: paidBy, amount, description: desc, category: selectedCat, split_among: splitAmong, split_type: splitType })
    });
    const data = await res.json();
    if (data.success) {
      showToast(`₹${amount} added! 💰`);
      const descEl   = document.getElementById('expDesc');
      const amountEl = document.getElementById('expAmount');
      if (descEl)   descEl.value   = '';
      if (amountEl) amountEl.value = '';
      loadExpenses();
    } else {
      showToast(data.error || 'Failed to add expense', 'error');
    }
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

async function loadExpenses() {
  if (!expGroupId) return;
  try {
    const res  = await fetch(`${API}/expenses/${expGroupId}`);
    const data = await res.json();
    renderExpenses(data.expenses    || []);
    renderExpSummary(data.summary   || {});
    renderSettlements(data.settlements || []);
  } catch(e) { showToast('Could not load expenses', 'error'); }
}

function renderExpenses(expenses) {
  const list = document.getElementById('expensesList');
  if (!list) return;
  if (expenses.length === 0) {
    list.innerHTML = `<div class="empty-expenses"><span class="empty-emoji">🧾</span><p>No expenses yet — add your first one above!</p></div>`;
    return;
  }
  const catIcons = { food:'🍜', transport:'🚗', hotel:'🏨', activities:'🎟️', shopping:'🛍️', other:'📦' };
  list.innerHTML = `<h3 style="font-family:var(--font-display);font-size:1rem;font-weight:700;margin-bottom:16px;">🧾 All Expenses (${expenses.length})</h3>` +
    expenses.slice().reverse().map(exp => `
      <div class="expense-card">
        <div class="expense-icon cat-${exp.category}">${catIcons[exp.category]||'📦'}</div>
        <div class="expense-info">
          <div class="expense-name">${exp.description}</div>
          <div class="expense-meta">Paid by <strong>${exp.paid_by}</strong> · Split: ${exp.split_among.join(', ')} · ${exp.date}</div>
        </div>
        <div class="expense-amount">₹${exp.amount.toLocaleString()}</div>
        <button class="expense-delete" onclick="deleteExp('${exp.id}')">✕</button>
      </div>`).join('');
}

function renderExpSummary(summary) {
  if (!summary.total_spent) return;
  setText('statTotal',       '₹' + (summary.total_spent||0).toLocaleString());
  setText('statPerPerson',   '₹' + (summary.per_person_avg||0).toLocaleString());
  setText('statCount',       summary.total_expenses||0);
  setText('statSettlements', Object.keys(summary.balances||{}).length);
  const balancesCard = document.getElementById('balancesCard');
  const balancesList = document.getElementById('balancesList');
  if (summary.balances && Object.keys(summary.balances).length > 0 && balancesCard && balancesList) {
    balancesCard.style.display = 'block';
    balancesList.innerHTML = Object.entries(summary.balances).map(([person, bal]) => `
      <div class="balance-row">
        <span>${person}</span>
        <span class="${bal>=0?'balance-positive':'balance-negative'}">${bal>=0?'+':''}₹${Math.abs(bal).toLocaleString()} ${bal>=0?'(gets back)':'(owes)'}</span>
      </div>`).join('');
  }
  if (summary.by_category && Object.keys(summary.by_category).length > 0) {
    const chartCard = document.getElementById('chartCard');
    if (chartCard) {
      chartCard.style.display = 'block';
      renderExpChart(summary.by_category);
    }
  }
  const shareCard = document.getElementById('shareCard');
  if (shareCard) shareCard.style.display = 'block';
}

function renderSettlements(settlements) {
  const card = document.getElementById('settlementsCard');
  const list = document.getElementById('settlementsList');
  if (!card || !list) return;
  if (settlements.length === 0) { card.style.display = 'none'; return; }
  card.style.display = 'block';
  list.innerHTML = settlements.map(s => `
    <div class="settlement-card">
      <span class="settlement-from">${s.from}</span>
      <span class="settlement-arrow">→ pays →</span>
      <span class="settlement-to">${s.to}</span>
      <span class="settlement-amount">₹${s.amount.toLocaleString()}</span>
    </div>`).join('');
}

function renderExpChart(byCategory) {
  if (!window.Chart) return;
  const ctx    = document.getElementById('expenseChart');
  if (!ctx) return;
  const labels = Object.keys(byCategory);
  const values = Object.values(byCategory);
  const colors = ['#ff6b35','#6c63ff','#43e97b','#ffd700','#ff6584','#a0a0b8'];
  if (expenseChart) expenseChart.destroy();
  expenseChart = new Chart(ctx.getContext('2d'), {
    type: 'doughnut',
    data: { labels, datasets: [{ data: values, backgroundColor: colors.slice(0, labels.length), borderWidth: 0, hoverOffset: 8 }] },
    options: { responsive: true, maintainAspectRatio: false,
      plugins: { legend: { position:'bottom', labels:{ color:'#a0a0b8', font:{size:12}, boxWidth:12, padding:16 } },
        tooltip: { callbacks: { label: ctx => ` ₹${ctx.raw.toLocaleString()}` } } } }
  });
}

async function deleteExp(expenseId) {
  if (!confirm('Delete this expense?')) return;
  try {
    const res  = await fetch(`${API}/expenses/delete/${expGroupId}/${expenseId}`, { method:'DELETE' });
    const data = await res.json();
    if (data.success) { showToast('Expense deleted'); loadExpenses(); }
  } catch(e) { showToast('Could not delete', 'error'); }
}

function shareExpenses() {
  const total = document.getElementById('statTotal')?.textContent || '₹0';
  const count = document.getElementById('statCount')?.textContent || '0';
  window.open(`https://wa.me/?text=${encodeURIComponent(`💰 *PackVote Expense Summary*\nGroup: ${expGroupId}\nTotal: ${total} across ${count} expenses\nSplit tracked with PackVote ✈`)}`, '_blank');
}

// ══════════════════════════════════════════════════════════════════════════
// PLANNER PAGE
// ══════════════════════════════════════════════════════════════════════════
let planGroupId  = '';
let planMembers  = [];
let allTasks     = [];
let activeFilter = 'all';
let activePerson = 'all';

const CAT_ICONS = { documents:'📄', bookings:'🎫', packing:'🧳', activities:'🎯', other:'📦' };

function initPlannerPage() {
  if (!document.getElementById('planGroupId')) return;
  const savedGroup = loadData('triply_group_id');
  const savedDest  = loadData('triply_winner') || '';
  if (savedGroup) {
    const planGroupEl = document.getElementById('planGroupId');
    const planDestEl  = document.getElementById('planDestination');
    if (planGroupEl) planGroupEl.value = savedGroup;
    if (planDestEl)  planDestEl.value  = savedDest;
    loadPlanner();
  }
}

async function loadPlanner() {
  const groupIdEl = document.getElementById('planGroupId');
  const groupId   = groupIdEl?.value.trim();
  if (!groupId) { showToast('Enter a group ID', 'error'); return; }
  planGroupId = groupId;
  saveData('triply_group_id', groupId);
  planMembers = loadData('triply_exp_members_' + groupId) || [];
  try {
    const res  = await fetch(`${API}/planner/${groupId}`);
    const data = await res.json();
    allTasks   = data.tasks || [];
    const generateWrap = document.getElementById('generateWrap');
    const addTaskForm  = document.getElementById('addTaskForm');
    const shareSection = document.getElementById('shareSection');
    if (generateWrap) generateWrap.style.display = 'block';
    if (addTaskForm)  addTaskForm.style.display   = 'block';
    if (shareSection) shareSection.style.display  = 'block';
    populatePlannerAssignees();
    renderTasks();
    updatePlannerStats(data.stats || {});
    renderPersonFilters();
    showToast(`Planner loaded! ${allTasks.length} tasks 📋`);
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

function populatePlannerAssignees() {
  const select = document.getElementById('taskAssignee');
  if (!select) return;
  select.innerHTML = '<option value="Unassigned">Unassigned</option>' +
    planMembers.map(m => `<option value="${m}">${m}</option>`).join('');
}

async function generateTasks() {
  const destination = document.getElementById('planDestination')?.value.trim() || 'your destination';
  const duration    = parseInt(document.getElementById('planDuration')?.value) || 7;
  if (!planGroupId) { showToast('Load planner first', 'error'); return; }
  if (allTasks.length > 0 && !confirm('Add default tasks to existing list?')) return;
  try {
    const res  = await fetch(`${API}/planner/generate`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_id: planGroupId, destination, duration, members: planMembers })
    });
    const data = await res.json();
    allTasks   = data.tasks || [];
    renderTasks();
    updatePlannerStats(data.stats || {});
    renderPersonFilters();
    showToast(`✨ ${allTasks.length} tasks generated!`);
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

async function addTask() {
  const title    = document.getElementById('taskTitle')?.value.trim();
  const desc     = document.getElementById('taskDesc')?.value.trim();
  const category = document.getElementById('taskCategory')?.value;
  const assignee = document.getElementById('taskAssignee')?.value;
  const priority = document.getElementById('taskPriority')?.value;
  const dueDate  = document.getElementById('taskDueDate')?.value;
  if (!title) { showToast('Enter a task title', 'error'); return; }
  try {
    const res  = await fetch(`${API}/planner/add`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_id: planGroupId, title, description: desc, category, assigned_to: assignee, priority, due_date: dueDate })
    });
    const data = await res.json();
    if (data.success) {
      allTasks.push(data.task);
      const titleEl = document.getElementById('taskTitle');
      const descEl  = document.getElementById('taskDesc');
      const dueEl   = document.getElementById('taskDueDate');
      if (titleEl) titleEl.value = '';
      if (descEl)  descEl.value  = '';
      if (dueEl)   dueEl.value   = '';
      renderTasks();
      refreshPlannerStats();
      showToast('Task added! ✅');
    }
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

async function toggleTask(taskId) {
  try {
    const res  = await fetch(`${API}/planner/toggle/${planGroupId}/${taskId}`, { method:'PUT' });
    const data = await res.json();
    if (data.success) {
      const task = allTasks.find(t => t.id === taskId);
      if (task) task.completed = data.completed;
      renderTasks();
      refreshPlannerStats();
    }
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

async function deleteTask(taskId) {
  if (!confirm('Delete this task?')) return;
  try {
    const res  = await fetch(`${API}/planner/delete/${planGroupId}/${taskId}`, { method:'DELETE' });
    const data = await res.json();
    if (data.success) {
      allTasks = allTasks.filter(t => t.id !== taskId);
      renderTasks();
      refreshPlannerStats();
      showToast('Task deleted');
    }
  } catch(e) { showToast('Cannot connect to server', 'error'); }
}

function renderTasks() {
  const list = document.getElementById('taskList');
  if (!list) return;
  let filtered = allTasks;
  if (activeFilter !== 'all') filtered = filtered.filter(t => t.category    === activeFilter);
  if (activePerson !== 'all') filtered = filtered.filter(t => t.assigned_to === activePerson);
  if (filtered.length === 0) {
    list.innerHTML = `<div class="empty-tasks"><span class="empty-emoji">✅</span><p>${allTasks.length===0?'No tasks yet — generate or add tasks above!':'No tasks match this filter.'}</p></div>`;
    return;
  }
  const categories = activeFilter === 'all' ? ['documents','bookings','packing','activities','other'] : [activeFilter];
  let html = '';
  for (const cat of categories) {
    const catTasks = filtered.filter(t => t.category === cat);
    if (catTasks.length === 0) continue;
    const done = catTasks.filter(t => t.completed).length;
    html += `
      <div class="task-category">
        <div class="task-category-header">
          <span class="task-category-icon">${CAT_ICONS[cat]||'📦'}</span>
          <span class="task-category-title">${capitalize(cat)}</span>
          <span class="task-category-progress">${done}/${catTasks.length}</span>
        </div>
        ${catTasks.map(task => {
          const pClass = `priority-${task.priority}`;
          const pLabel = task.priority==='high'?'🔴 High':task.priority==='medium'?'🟡 Medium':'🟢 Low';
          return `
            <div class="task-item ${task.completed?'completed':''}" id="task_${task.id}">
              <div class="task-check" onclick="toggleTask('${task.id}')">${task.completed?'✓':''}</div>
              <div class="task-content">
                <div class="task-title">${task.title}</div>
                ${task.description?`<div class="task-desc">${task.description}</div>`:''}
                <div class="task-meta">
                  <span class="task-assignee">👤 ${task.assigned_to}</span>
                  <span class="task-priority ${pClass}">${pLabel}</span>
                  ${task.due_date?`<span class="task-due">📅 ${task.due_date}</span>`:''}
                </div>
              </div>
              <button class="task-delete" onclick="deleteTask('${task.id}')">✕</button>
            </div>`;
        }).join('')}
      </div>`;
  }
  list.innerHTML = html;
  updatePlannerCounts();
}

function filterTasks(filter, btn) {
  activeFilter = filter; activePerson = 'all';
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.person-filter-btn').forEach(b => b.classList.remove('active'));
  renderTasks();
}

function filterByPerson(person, btn) {
  activePerson = person; activeFilter = 'all';
  document.querySelectorAll('.filter-btn,.person-filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderTasks();
}

async function refreshPlannerStats() {
  try {
    const res  = await fetch(`${API}/planner/${planGroupId}`);
    const data = await res.json();
    updatePlannerStats(data.stats || {});
    renderPersonFilters();
  } catch(e) {}
}

function updatePlannerStats(stats) {
  const pct = stats.percentage || 0;
  setText('progressPct',   pct + '%');
  setText('progressLabel', `${stats.completed||0} of ${stats.total||0} tasks done`);
  const mainFill = document.getElementById('mainProgressFill');
  if (mainFill) mainFill.style.width = pct + '%';
  const section = document.getElementById('personStatsSection');
  const psDiv   = document.getElementById('personStats');
  if (stats.by_person && Object.keys(stats.by_person).length > 0 && section && psDiv) {
    section.style.display = 'block';
    psDiv.innerHTML = Object.entries(stats.by_person).map(([person, data]) => {
      const pct = data.total > 0 ? Math.round((data.completed/data.total)*100) : 0;
      return `<div class="person-stat">
        <span style="font-size:0.85rem;">${person}</span>
        <div class="person-stat-bar"><div class="person-stat-fill" style="width:${pct}%"></div></div>
        <span style="font-size:0.78rem;color:var(--text-muted);">${data.completed}/${data.total}</span>
      </div>`;
    }).join('');
  }
  updatePlannerCounts();
}

function updatePlannerCounts() {
  const cats = ['documents','bookings','packing','activities','other'];
  setText('countAll', allTasks.length);
  cats.forEach(cat => {
    const el = document.getElementById('count' + capitalize(cat));
    if (el) el.textContent = allTasks.filter(t => t.category === cat).length;
  });
}

function renderPersonFilters() {
  const container = document.getElementById('personFilters');
  if (!container) return;
  const people = [...new Set(allTasks.map(t => t.assigned_to))];
  if (people.length === 0) {
    container.innerHTML = '<p style="font-size:0.82rem;color:var(--text-muted);">No tasks assigned yet</p>';
    return;
  }
  container.innerHTML = `
    <button class="filter-btn person-filter-btn active" onclick="filterByPerson('all', this)">
      👥 Everyone <span class="filter-count">${allTasks.length}</span>
    </button>` +
    people.map(p => `
      <button class="filter-btn person-filter-btn" onclick="filterByPerson('${p}', this)">
        👤 ${p} <span class="filter-count">${allTasks.filter(t=>t.assigned_to===p).length}</span>
      </button>`).join('');
}

function sharePlanner() {
  const done    = allTasks.filter(t => t.completed).length;
  const total   = allTasks.length;
  const pending = allTasks.filter(t => !t.completed).slice(0,5).map(t => `• ${t.title} (${t.assigned_to})`).join('\n');
  window.open(`https://wa.me/?text=${encodeURIComponent(`✅ *PackVote Trip Planner*\nProgress: ${done}/${total} tasks done\n\n*Pending:*\n${pending}\n\nPlanned with PackVote ✈`)}`, '_blank');
}

// ══════════════════════════════════════════════════════════════════════════
// AUTO INIT
// ══════════════════════════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  initVotePage();
  initResultsPage();
  initExpensesPage();
  initPlannerPage();

  const memberInput = document.getElementById('memberInput');
  if (memberInput) memberInput.addEventListener('keypress', e => { if (e.key==='Enter') addMember(); });

  const expMemberInput = document.getElementById('expMemberInput');
  if (expMemberInput) expMemberInput.addEventListener('keypress', e => { if (e.key==='Enter') addExpMember(); });

  const taskTitleInput = document.getElementById('taskTitle');
  if (taskTitleInput) taskTitleInput.addEventListener('keypress', e => { if (e.key==='Enter') addTask(); });

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity   = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.how-step, .dest-img-card, .feature-card').forEach(el => {
    el.style.opacity    = '0';
    el.style.transform  = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
});