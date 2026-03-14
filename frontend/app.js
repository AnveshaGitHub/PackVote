const API = 'http://127.0.0.1:5000/api';

// ── Destination images (Unsplash — free) ──────────────────────────────────
const DEST_IMAGES = {
  'Mumbai':      'https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&q=80',
  'Delhi':       'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&q=80',
  'Jaipur':      'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800&q=80',
  'Goa':         'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800&q=80',
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
  'Ooty':        'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&q=80',
  'Munnar':      'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800&q=80',
  'Gangtok':     'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
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

function getDestImage(name) {
  return DEST_IMAGES[name] || DEST_IMAGES['default'];
}

// ── Destination descriptions ──────────────────────────────────────────────
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
  'Darjeeling': 'Queen of hills — tea estates and Tiger Hill sunrise',
  'Coorg':      'Scotland of India — coffee estates and misty hills',
  'Jaisalmer':  'Golden city rising from the Thar Desert',
  'Paris':      'City of lights, art and cuisine',
  'Tokyo':      'Ultra-modern meets ancient tradition',
  'Bali':       'Tropical paradise with rich spiritual culture',
  'Dubai':      'City of superlatives — tallest, largest, most luxurious',
  'Maldives':   'Paradise overwater bungalows and crystal seas',
};

function getDestDesc(name) {
  return DEST_DESCS[name] || 'An incredible destination awaits your group!';
}

// ── Destination coordinates ───────────────────────────────────────────────
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
  'Pondicherry':[11.9416, 79.8083],
  'Coorg':      [12.3375, 75.8069],
  'Jaisalmer':  [26.9157, 70.9083],
  'Mysuru':     [12.2958, 76.6394],
  'Ooty':       [11.4102, 76.6950],
  'Munnar':     [10.0889, 77.0595],
  'Paris':      [48.8566,  2.3522],
  'Tokyo':      [35.6762,139.6503],
  'Bali':       [-8.3405,115.0920],
  'Dubai':      [25.2048, 55.2708],
  'London':     [51.5074, -0.1278],
  'Singapore':  [ 1.3521,103.8198],
  'Maldives':   [ 3.2028, 73.2207],
  'Bangkok':    [13.7563,100.5018],
};

function getDestCoords(name) {
  return DEST_COORDS[name] || [20.5937, 78.9629];
}

// ══════════════════════════════════════════════════════════════════════════
// TOAST NOTIFICATIONS
// ══════════════════════════════════════════════════════════════════════════
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

// ── localStorage helpers ──────────────────────────────────────────────────
function saveData(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}
function loadData(key) {
  try { return JSON.parse(localStorage.getItem(key)); }
  catch { return null; }
}
function capitalize(s) {
  return s ? s.charAt(0).toUpperCase() + s.slice(1) : '—';
}
function setText(id, val) {
  const el = document.getElementById(id);
  if (el) el.textContent = val;
}

// ── Auth guard — redirect to login if not logged in ───────────────────────
function requireAuth() {
  const user = loadData('triply_user');
  if (!user) {
    window.location.href = 'login.html';
    return null;
  }
  return user;
}

// ══════════════════════════════════════════════════════════════════════════
// INDEX PAGE — Group creation
// ══════════════════════════════════════════════════════════════════════════
let members = [];

function addMember() {
  const input = document.getElementById('memberInput');
  if (!input) return;
  const name = input.value.trim();
  if (!name) { showToast('Please enter a name', 'error'); return; }
  if (members.includes(name)) { showToast('Member already added', 'error'); return; }
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
    </div>
  `).join('');
}

function removeMember(name) {
  members = members.filter(m => m !== name);
  renderMembers();
}

async function createGroup() {
  const user      = loadData('triply_user');
  const groupName = document.getElementById('groupName')?.value.trim();
  if (!groupName)        { showToast('Please enter a group name', 'error'); return; }
  if (members.length < 1){ showToast('Add at least 1 member', 'error'); return; }

  try {
    const res  = await fetch(`${API}/group/create`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        group_name: groupName,
        members,
        user_id: user?.user_id || ''
      })
    });
    const data = await res.json();
    if (data.success) {
      saveData('triply_group_id',   data.group_id);
      saveData('triply_group_name', data.group_name);

      // Update user's groups in localStorage
      if (user) {
        if (!user.groups) user.groups = [];
        user.groups.push({
          group_id:   data.group_id,
          group_name: data.group_name,
          joined_at:  new Date().toISOString()
        });
        saveData('triply_user', user);
      }

      showToast(`Group "${groupName}" created! 🎉`);
      setTimeout(() => window.location.href = 'vote.html', 1200);
    }
  } catch(e) {
    showToast('Could not connect to server. Is Flask running?', 'error');
  }
}

// ══════════════════════════════════════════════════════════════════════════
// VOTE PAGE
// ══════════════════════════════════════════════════════════════════════════
const VOTE_DESTINATIONS = [
  { name: 'Jaipur',     desc: 'The Pink City — palaces, forts and vibrant bazaars',      tags: ['history','culture','food','shopping'], cost: '₹3,500/day' },
  { name: 'Goa',        desc: "India's beach paradise — sun, seafood and parties",        tags: ['beach','nightlife','food','adventure'], cost: '₹5,000/day' },
  { name: 'Kerala',     desc: 'Backwaters, tea gardens and Ayurvedic retreats',           tags: ['nature','wellness','romance','culture'],cost: '₹4,000/day' },
  { name: 'Manali',     desc: 'Adventure capital — skiing, trekking and Rohtang Pass',   tags: ['adventure','nature','romance'],         cost: '₹4,500/day' },
  { name: 'Varanasi',   desc: 'Oldest living city — ghats, rituals and spiritual energy',tags: ['culture','history','wellness','food'],  cost: '₹2,500/day' },
  { name: 'Leh Ladakh', desc: 'Roof of the world — monasteries and mountain passes',     tags: ['adventure','nature','culture'],         cost: '₹4,500/day' },
  { name: 'Udaipur',    desc: 'City of lakes — the most romantic city in India',         tags: ['romance','history','culture','art'],    cost: '₹4,000/day' },
  { name: 'Rishikesh',  desc: 'Yoga capital — river rafting and Ganges ghats',           tags: ['wellness','adventure','culture'],       cost: '₹2,500/day' },
  { name: 'Hampi',      desc: 'UNESCO ruins of the Vijayanagara Empire amid boulders',   tags: ['history','culture','adventure','art'],  cost: '₹2,000/day' },
  { name: 'Srinagar',   desc: 'Paradise on earth — Dal Lake houseboats and gardens',     tags: ['romance','nature','culture','history'], cost: '₹4,500/day' },
];

let currentCardIndex = 0;
let votedDestinations = [];
let selectedBudget    = 'medium';
let selectedStyles    = [];

function initVotePage() {
  if (!document.getElementById('cardStack')) return;

  // Pre-fill group ID and voter name from saved data
  const savedGroup = loadData('triply_group_id');
  const savedUser  = loadData('triply_user');
  if (savedGroup) {
    const el = document.getElementById('groupId');
    if (el) el.value = savedGroup;
  }
  if (savedUser) {
    const el = document.getElementById('voterName');
    if (el) el.value = savedUser.name || '';
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
      </div>
    `;
    stack.appendChild(card);
    if (isTop) initDrag(card);
  });
  updateProgress();
}

function initDrag(card) {
  let startX = 0, currentX = 0, isDragging = false;

  card.addEventListener('mousedown', e => {
    isDragging = true;
    startX = e.clientX;
    card.style.transition = 'none';
  });

  document.addEventListener('mousemove', e => {
    if (!isDragging) return;
    currentX = e.clientX - startX;
    card.style.transform = `translateX(${currentX}px) rotate(${currentX * 0.04}deg)`;
    const like = card.querySelector('.like-stamp');
    const nope = card.querySelector('.nope-stamp');
    if (like) like.style.opacity = currentX > 40 ? Math.min((currentX - 40) / 80, 1) : 0;
    if (nope) nope.style.opacity = currentX < -40 ? Math.min((-currentX - 40) / 80, 1) : 0;
  });

  document.addEventListener('mouseup', () => {
    if (!isDragging) return;
    isDragging = false;
    if      (currentX >  90) animateCard(card, 'love');
    else if (currentX < -90) animateCard(card, 'skip');
    else {
      card.style.transition = 'transform 0.4s ease';
      card.style.transform  = '';
    }
    currentX = 0;
  });

  // Touch
  card.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
    card.style.transition = 'none';
  });
  card.addEventListener('touchmove', e => {
    currentX = e.touches[0].clientX - startX;
    card.style.transform = `translateX(${currentX}px) rotate(${currentX * 0.04}deg)`;
    const like = card.querySelector('.like-stamp');
    const nope = card.querySelector('.nope-stamp');
    if (like) like.style.opacity = currentX > 40 ? Math.min((currentX - 40) / 80, 1) : 0;
    if (nope) nope.style.opacity = currentX < -40 ? Math.min((-currentX - 40) / 80, 1) : 0;
  });
  card.addEventListener('touchend', () => {
    if      (currentX >  90) animateCard(card, 'love');
    else if (currentX < -90) animateCard(card, 'skip');
    else {
      card.style.transition = 'transform 0.4s ease';
      card.style.transform  = '';
    }
    currentX = 0;
  });
}

function animateCard(card, direction) {
  const dest = VOTE_DESTINATIONS[currentCardIndex];
  const xOut = direction === 'love' ? 900 : -900;

  card.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
  card.style.transform  = `translateX(${xOut}px) rotate(${direction === 'love' ? 25 : -25}deg)`;
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
  if (topCard && topCard.classList.contains('v-card')) {
    animateCard(topCard, direction);
  } else {
    showDoneState();
  }
}

function updateProgress() {
  const pct     = Math.round((currentCardIndex / VOTE_DESTINATIONS.length) * 100);
  const fill    = document.getElementById('progressFill');
  const counter = document.getElementById('voteCounter');
  if (fill)    fill.style.width   = pct + '%';
  if (counter) counter.textContent= `Swipe or use buttons · ${currentCardIndex} / ${VOTE_DESTINATIONS.length} voted`;
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
  const groupId   = document.getElementById('groupId')?.value.trim()
                    || loadData('triply_group_id');
  const duration  = parseInt(document.getElementById('duration')?.value || '7');
  const month     = document.getElementById('month')?.value || 'December';

  if (!voterName) { showToast('Please enter your name', 'error'); return; }
  if (!groupId)   { showToast('Please enter a Group ID', 'error'); return; }

  const preferences = {
    destinations:  votedDestinations.length > 0
                   ? votedDestinations
                   : ['Jaipur','Goa','Kerala'],
    budget:        selectedBudget,
    travel_style:  selectedStyles.length > 0
                   ? selectedStyles
                   : ['culture','food'],
    duration,
    month
  };

  try {
    const res  = await fetch(`${API}/vote/submit`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        group_id:    groupId,
        user_name:   voterName,
        preferences
      })
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
  } catch(e) {
    showToast('Could not connect to server', 'error');
  }
}

// ══════════════════════════════════════════════════════════════════════════
// RESULTS PAGE
// ══════════════════════════════════════════════════════════════════════════
let triplyMap = null;

async function initResultsPage() {
  if (!document.getElementById('winnerName')) return;

  const groupId = loadData('triply_group_id');
  if (!groupId) { loadDemoResults(); return; }

  try {
    const res  = await fetch(`${API}/vote/results/${groupId}`);
    const data = await res.json();
    if (data.error) { loadDemoResults(); return; }
    renderResults(data);
    const winner = data.consensus?.winner;
    if (winner) {
      await loadWeather(winner);
      await loadItinerary(winner, data.consensus);
    }
  } catch(e) {
    loadDemoResults();
  }
}

function loadDemoResults() {
  const demo = {
    group_name:  'Demo Group',
    total_votes: 3,
    consensus: {
      winner: 'Jaipur',
      top_destinations: [
        { destination: 'Jaipur',  percentage: 100 },
        { destination: 'Goa',     percentage: 78  },
        { destination: 'Kerala',  percentage: 65  },
        { destination: 'Manali',  percentage: 50  },
        { destination: 'Udaipur', percentage: 40  },
      ],
      consensus_budget: 'medium',
      avg_duration:     7,
      consensus_month:  'December',
      top_styles:       ['culture','food','adventure'],
      conflicts:        []
    },
    recommendations: [
      { destination: 'Jaipur',  match_percentage: 95, description: 'The Pink City',  avg_cost_per_day: 3500, tags: ['history','culture','food'] },
      { destination: 'Udaipur', match_percentage: 88, description: 'City of Lakes',  avg_cost_per_day: 4000, tags: ['romance','history'] },
      { destination: 'Jodhpur', match_percentage: 82, description: 'The Blue City',  avg_cost_per_day: 3000, tags: ['history','culture'] },
    ]
  };
  renderResults(demo);
  loadWeather('Jaipur');
  loadItinerary('Jaipur', demo.consensus);
}

function renderResults(data) {
  const c = data.consensus;

  // Winner hero
  setText('winnerName', c.winner || 'Your Destination');
  setText('winnerDesc', getDestDesc(c.winner));
  const bgImg = document.getElementById('winnerBgImg');
  if (bgImg) bgImg.src = getDestImage(c.winner);

  // Stats
  setText('statVoters', data.total_votes);
  setText('statDays',   (c.avg_duration || '—') + (c.avg_duration ? 'd' : ''));
  setText('statBudget', capitalize(c.consensus_budget));
  setText('statMonth',  c.consensus_month?.slice(0,3) || '—');

  // Score bars
  const scoreList = document.getElementById('scoreList');
  if (scoreList && c.top_destinations) {
    scoreList.innerHTML = c.top_destinations.map((d, i) => `
      <div class="score-bar">
        <div class="score-label">${i === 0 ? '🏆' : `#${i+1}`} ${d.destination}</div>
        <div class="score-track">
          <div class="score-fill" style="width:0%"
               data-pct="${d.percentage}"></div>
        </div>
        <div class="score-pct">${d.percentage}%</div>
      </div>
    `).join('');
    setTimeout(() => {
      document.querySelectorAll('.score-fill').forEach(el => {
        el.style.width = el.dataset.pct + '%';
      });
    }, 400);
  }

  // Recommendations
  const recList = document.getElementById('recList');
  if (recList && data.recommendations) {
    recList.innerHTML = data.recommendations.map((r, i) => `
      <div class="rec-card">
        <div class="rec-rank ${i === 0 ? 'top' : ''}">
          ${i === 0 ? '🥇' : i === 1 ? '🥈' : '🥉'}
        </div>
        <img src="${getDestImage(r.destination)}"
             style="width:56px;height:56px;border-radius:10px;object-fit:cover;flex-shrink:0;"
             alt="${r.destination}"/>
        <div class="rec-info">
          <div class="rec-name">${r.destination}</div>
          <div class="rec-desc">${r.description}</div>
          <div class="rec-meta">
            <span>₹${(r.avg_cost_per_day || 0).toLocaleString()}/day</span>
            <span>${(r.tags || []).slice(0,2).join(' · ')}</span>
          </div>
        </div>
        <div class="rec-match">${r.match_percentage}%</div>
      </div>
    `).join('');
  }

  // Conflicts
  if (c.conflicts && c.conflicts.length > 0) {
    const section = document.getElementById('conflictSection');
    const list    = document.getElementById('conflictList');
    if (section) section.style.display = 'block';
    if (list) list.innerHTML = c.conflicts.map(cf => `
      <div class="conflict-alert">
        <span class="conflict-icon">${cf.severity === 'high' ? '🔴' : '🟡'}</span>
        <span class="conflict-text">${cf.message}</span>
      </div>
    `).join('');
  }

  // Map
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
            ${(f.description || '').split(' ').slice(0,2).join(' ')}
          </div>
        </div>
      `).join('');
    }
  } catch(e) {
    setText('weatherDesc', 'Weather data unavailable');
  }
}

async function loadItinerary(destination, consensus) {
  try {
    const res  = await fetch(`${API}/itinerary/generate`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        destination,
        duration:     consensus.avg_duration || 7,
        budget:       consensus.consensus_budget || 'medium',
        travel_style: consensus.top_styles || ['culture'],
        month:        consensus.consensus_month || 'December'
      })
    });
    const data = await res.json();
    if (data.itinerary) {
      renderCost(data.itinerary.estimated_cost);
      renderItinerary(data.itinerary);
    }
  } catch(e) {
    renderFallbackItinerary(destination);
  }
}

function renderCost(cost) {
  const grid = document.getElementById('costGrid');
  if (!grid || !cost?.per_person) return;
  const p = cost.per_person;
  grid.innerHTML = `
    <div class="cost-item">
      <div class="cost-item-label">✈️ Flights</div>
      <div class="cost-item-value">₹${(p.flights||0).toLocaleString()}</div>
    </div>
    <div class="cost-item">
      <div class="cost-item-label">🏨 Hotel</div>
      <div class="cost-item-value">₹${(p.accommodation||0).toLocaleString()}</div>
    </div>
    <div class="cost-item">
      <div class="cost-item-label">🍜 Food</div>
      <div class="cost-item-value">₹${(p.food||0).toLocaleString()}</div>
    </div>
    <div class="cost-item">
      <div class="cost-item-label">🎟️ Activities</div>
      <div class="cost-item-value">₹${(p.activities||0).toLocaleString()}</div>
    </div>
    <div class="cost-item" style="grid-column:span 2;border-color:rgba(255,215,0,0.3);">
      <div class="cost-item-label">💰 Total per person</div>
      <div class="cost-item-value" style="font-size:1.8rem;">
        ₹${(p.total||0).toLocaleString()}
      </div>
    </div>
  `;
}

function renderItinerary(itinerary) {
  const list = document.getElementById('itineraryList');
  if (!list) return;
  const days = itinerary.days || [];
  if (days.length === 0) {
    renderFallbackItinerary(itinerary.destination);
    return;
  }
  list.innerHTML = days.map(day => `
    <div class="day-card">
      <div class="day-header" onclick="toggleDay(this)">
        <div class="day-number">D${day.day}</div>
        <div>
          <div class="day-title">${day.title}</div>
          <div style="font-size:0.8rem;color:var(--text-muted);">
            ${(day.activities||[]).length} activities planned
          </div>
        </div>
        <span style="margin-left:auto;color:var(--text-muted);">▾</span>
      </div>
      <div class="day-body">
        ${(day.activities||[]).map(a => `
          <div class="activity">
            <div class="activity-dot"></div>
            <div>
              <div class="activity-name">${a.name || 'Local Exploration'}</div>
              <div class="activity-type">
                ${a.type || 'experience'}
                ${a.opening_hours ? ' · ' + a.opening_hours : ''}
              </div>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `).join('');
}

function renderFallbackItinerary(destination) {
  const list = document.getElementById('itineraryList');
  if (!list) return;
  renderItinerary({
    destination,
    days: [
      { day:1, title:'Arrival & Exploration',  activities:[{name:'Check in & freshen up',type:'accommodation'},{name:'Evening walk around city centre',type:'sightseeing'},{name:'Welcome dinner at local restaurant',type:'food'}] },
      { day:2, title:'Main Attractions',        activities:[{name:'Visit top historical sites',type:'sightseeing'},{name:'Local market tour',type:'shopping'},{name:'Street food lunch',type:'food'}] },
      { day:3, title:'Culture & Heritage',      activities:[{name:'Museum visit',type:'culture'},{name:'Art gallery',type:'art'},{name:'Traditional dinner',type:'food'}] },
      { day:4, title:'Adventure Day',           activities:[{name:'Guided city tour',type:'tour'},{name:'Adventure activity',type:'adventure'},{name:'Rooftop dinner',type:'food'}] },
      { day:5, title:'Leisure & Departure',     activities:[{name:'Morning at leisure',type:'relaxation'},{name:'Last minute shopping',type:'shopping'},{name:'Farewell dinner',type:'food'}] },
    ]
  });
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
    className: '',
    iconSize:   [40, 40],
    iconAnchor: [20, 20]
  });

  L.marker(coords, { icon })
   .addTo(triplyMap)
   .bindPopup(`<b>${destination}</b><br>Your group's destination! 🎉`)
   .openPopup();
}

// ── Share functions ───────────────────────────────────────────────────────
function shareWhatsApp() {
  const winner = document.getElementById('winnerName')?.textContent || 'our destination';
  const text   = encodeURIComponent(
    `🌍 Our group is going to *${winner}*!\nPlanned with Triply ✈\nVote. Plan. Fly.`
  );
  window.open(`https://wa.me/?text=${text}`, '_blank');
}

function copyLink() {
  navigator.clipboard.writeText(window.location.href);
  showToast('Link copied! 🔗');
}

// ══════════════════════════════════════════════════════════════════════════
// AUTO INIT — runs on every page
// ══════════════════════════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  initVotePage();
  initResultsPage();

  // Enter key for member input on index page
  const memberInput = document.getElementById('memberInput');
  if (memberInput) {
    memberInput.addEventListener('keypress', e => {
      if (e.key === 'Enter') addMember();
    });
  }

  // Scroll animations
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity    = '1';
        entry.target.style.transform  = 'translateY(0)';
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