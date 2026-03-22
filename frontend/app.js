const API = 'http://127.0.0.1:5000/api';

const DEST_IMAGES = {
  'Mumbai':'https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&q=80',
  'Delhi':'https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&q=80',
  'Jaipur':'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800&q=80',
  'Goa':'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1600&q=80',
  'Kerala':'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800&q=80',
  'Manali':'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80',
  'Agra':'https://images.unsplash.com/photo-1548013146-72479768bada?w=800&q=80',
  'Varanasi':'https://images.unsplash.com/photo-1561361058-c24e01c78e6e?w=800&q=80',
  'Udaipur':'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&q=80',
  'Mysuru':'https://images.unsplash.com/photo-1580181591840-b5f3f9b27d16?w=800&q=80',
  'Rishikesh':'https://images.unsplash.com/photo-1600697395543-31e0c3a25dbd?w=800&q=80',
  'Leh Ladakh':'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
  'Shimla':'https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&q=80',
  'Hampi':'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&q=80',
  'Darjeeling':'https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&q=80',
  'Pondicherry':'https://images.unsplash.com/photo-1617469767053-d3b523a0b982?w=800&q=80',
  'Srinagar':'https://images.unsplash.com/photo-1602532305019-3dbbd482dae7?w=800&q=80',
  'Coorg':'https://images.unsplash.com/photo-1582053433976-25c00369831c?w=800&q=80',
  'Jaisalmer':'https://images.unsplash.com/photo-1612214248522-5c09f1be0a2e?w=800&q=80',
  'Alleppey':'https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=800&q=80',
  'Paris':'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80',
  'Tokyo':'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80',
  'Bali':'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80',
  'Bangkok':'https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=800&q=80',
  'Dubai':'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80',
  'Singapore':'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800&q=80',
  'Maldives':'https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800&q=80',
  'London':'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800&q=80',
  'Nepal':'https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&q=80',
  'Sri Lanka':'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&q=80',
  'default':'https://images.unsplash.com/photo-1488085061387-422e29b40080?w=800&q=80'
};

const DEST_DESCS = {
  'Jaipur':'The Pink City — palaces, forts and vibrant bazaars',
  'Goa':"India's beach paradise — sun, seafood and parties",
  'Kerala':'Backwaters, tea gardens and Ayurvedic retreats',
  'Manali':'Adventure capital — skiing, trekking and mountain passes',
  'Varanasi':'Oldest living city — ghats, rituals and spiritual energy',
  'Udaipur':'City of lakes — the most romantic city in India',
  'Leh Ladakh':'Roof of the world — monasteries and mountain passes',
  'Rishikesh':'Yoga capital — river rafting and Ganges ghats',
  'Srinagar':'Paradise on earth — Dal Lake houseboats and gardens',
  'Delhi':"India's capital — Mughal monuments and chaotic bazaars",
  'Mumbai':'City of dreams — Bollywood, street food and the sea',
  'Agra':'Home of the Taj Mahal — Mughal architecture at its finest',
  'Hampi':'UNESCO ruins of the Vijayanagara Empire amid boulders',
  'Coorg':'Scotland of India — coffee estates and misty hills',
  'Jaisalmer':'Golden city rising from the Thar Desert',
  'Paris':'City of lights, art and cuisine',
  'Tokyo':'Ultra-modern meets ancient tradition',
  'Bali':'Tropical paradise with rich spiritual culture',
  'Dubai':'City of superlatives — tallest, largest, most luxurious',
  'Maldives':'Paradise overwater bungalows and crystal seas',
};

const DEST_COORDS = {
  'Jaipur':[26.9124,75.7873],'Goa':[15.2993,74.1240],'Kerala':[10.8505,76.2711],
  'Mumbai':[19.0760,72.8777],'Delhi':[28.7041,77.1025],'Manali':[32.2396,77.1887],
  'Agra':[27.1767,78.0081],'Varanasi':[25.3176,82.9739],'Udaipur':[24.5854,73.7125],
  'Leh Ladakh':[34.1526,77.5770],'Rishikesh':[30.0869,78.2676],'Srinagar':[34.0837,74.7973],
  'Shimla':[31.1048,77.1734],'Darjeeling':[27.0360,88.2627],'Hampi':[15.3350,76.4600],
  'Coorg':[12.3375,75.8069],'Jaisalmer':[26.9157,70.9083],'Mysuru':[12.2958,76.6394],
  'Paris':[48.8566,2.3522],'Tokyo':[35.6762,139.6503],'Bali':[-8.3405,115.0920],
  'Dubai':[25.2048,55.2708],'London':[51.5074,-0.1278],'Singapore':[1.3521,103.8198],
  'Maldives':[3.2028,73.2207],'Bangkok':[13.7563,100.5018],
};

// ── Utilities ──────────────────────────────────────────────────────────────
function getDestImage(name)  { return DEST_IMAGES[name]  || DEST_IMAGES['default']; }
function getDestDesc(name)   { return DEST_DESCS[name]   || 'An incredible destination awaits!'; }
function getDestCoords(name) { return DEST_COORDS[name]  || [20.5937,78.9629]; }
function capitalize(s)       { return s ? s.charAt(0).toUpperCase()+s.slice(1) : '—'; }
function setText(id,val)     { const el=document.getElementById(id); if(el) el.textContent=val; }
function saveData(key,val)   { localStorage.setItem(key,JSON.stringify(val)); }
function loadData(key)       { try{return JSON.parse(localStorage.getItem(key));}catch{return null;} }

// ── Session — only user object stored, NO group data in localStorage ────────
function saveUser(user) { localStorage.setItem('PackVote_user',JSON.stringify(user)); }
function loadUser()     { try{return JSON.parse(localStorage.getItem('PackVote_user'));}catch{return null;} }

// ── Toast ──────────────────────────────────────────────────────────────────
function showToast(message, type='success') {
  const container = document.getElementById('toastContainer');
  if(!container) return;
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${type==='success'?'✅':'❌'}</span> ${message}`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.animation = 'slideOut 0.3s ease forwards';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// ── Auth ───────────────────────────────────────────────────────────────────
function requireAuth() {
  const user = loadUser();
  if(!user || !user.user_id) { window.location.href='login.html'; return null; }
  return user;
}

function logout() {
  localStorage.clear();
  showToast('Logged out 👋');
  setTimeout(() => window.location.href='login.html', 800);
}

// ── DB helpers — group data always from API ─────────────────────────────────
async function fetchActiveGroup(userId) {
  try {
    const res  = await fetch(`${API}/auth/user/${userId}/groups`);
    const data = await res.json();
    const groups = data.groups || [];
    if(groups.length === 0) return null;
    return groups[0]; // most recent group
  } catch(e) { console.error('fetchActiveGroup error:',e); return null; }
}

async function fetchGroupDetails(groupId) {
  try {
    const res = await fetch(`${API}/group/${groupId}`);
    return await res.json();
  } catch(e) { console.error('fetchGroupDetails error:',e); return null; }
}

// ══════════════════════════════════════════════════════════════════════════
// INDEX PAGE
// ══════════════════════════════════════════════════════════════════════════
let members = [];

async function initIndexPage() {
  if(!document.getElementById('groupName')) return;
  const user = requireAuth();
  if(!user) return;
}

function addMember() {
  const input = document.getElementById('memberInput');
  if(!input) return;
  const name = input.value.trim();
  if(!name)                  { showToast('Please enter a name','error'); return; }
  if(members.includes(name)) { showToast('Already added!','error'); return; }
  members.push(name);
  input.value = '';
  renderMembers();
  showToast(`${name} added! ✅`);
}

function renderMembers() {
  const list = document.getElementById('membersList');
  if(!list) return;
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
  const user      = loadUser();
  const groupName = document.getElementById('groupName')?.value.trim();
  if(!groupName)         { showToast('Enter a group name','error'); return; }
  if(members.length < 1) { showToast('Add at least 1 member','error'); return; }
  try {
    const res  = await fetch(`${API}/group/create`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ group_name:groupName, members, user_id:user?.user_id||'' })
    });
    const data = await res.json();
    if(data.success) {
      showToast(`"${groupName}" created! 🎉`);
      setTimeout(() => window.location.href='dashboard.html', 1200);
    } else { showToast(data.error||'Failed to create group','error'); }
  } catch(e) { showToast('Cannot connect to server. Is Flask running?','error'); }
}

// ══════════════════════════════════════════════════════════════════════════
// VOTE PAGE
// ══════════════════════════════════════════════════════════════════════════
const VOTE_DESTINATIONS = [
  {name:'Jaipur',    desc:'The Pink City — palaces, forts and vibrant bazaars',       tags:['history','culture','food','shopping'],cost:'₹3,500/day'},
  {name:'Goa',       desc:"India's beach paradise — sun, seafood and parties",         tags:['beach','nightlife','food','adventure'], cost:'₹5,000/day'},
  {name:'Kerala',    desc:'Backwaters, tea gardens and Ayurvedic retreats',            tags:['nature','wellness','romance','culture'],cost:'₹4,000/day'},
  {name:'Manali',    desc:'Adventure capital — skiing, trekking and Rohtang Pass',    tags:['adventure','nature','romance'],         cost:'₹4,500/day'},
  {name:'Varanasi',  desc:'Oldest living city — ghats, rituals and spiritual energy', tags:['culture','history','wellness'],         cost:'₹2,500/day'},
  {name:'Leh Ladakh',desc:'Roof of the world — monasteries and mountain passes',      tags:['adventure','nature','culture'],         cost:'₹4,500/day'},
  {name:'Udaipur',   desc:'City of lakes — the most romantic city in India',          tags:['romance','history','culture','art'],    cost:'₹4,000/day'},
  {name:'Rishikesh', desc:'Yoga capital — river rafting and Ganges ghats',            tags:['wellness','adventure','culture'],       cost:'₹2,500/day'},
  {name:'Hampi',     desc:'UNESCO ruins of the Vijayanagara Empire amid boulders',    tags:['history','culture','adventure','art'],  cost:'₹2,000/day'},
  {name:'Srinagar',  desc:'Paradise on earth — Dal Lake houseboats and gardens',      tags:['romance','nature','culture','history'], cost:'₹4,500/day'},
  {name:'Coorg',     desc:'Scotland of India — coffee estates and misty hills',       tags:['nature','adventure','wellness'],        cost:'₹3,500/day'},
  {name:'Jaisalmer', desc:'Golden city rising from the Thar Desert',                  tags:['history','adventure','culture'],        cost:'₹3,000/day'},
];

let currentCardIndex=0, votedDestinations=[], selectedBudget='medium';
let selectedDuration=7, selectedStyles=[], activeGroupId=null;

async function initVotePage() {
  if(!document.getElementById('cardStack')) return;
  const user = requireAuth();
  if(!user) return;
  const group = await fetchActiveGroup(user.user_id);
  if(!group) {
    showToast('No group found. Create or join a group first.','error');
    setTimeout(() => window.location.href='dashboard.html', 1500);
    return;
  }
  activeGroupId = group.group_id;
  const groupEl = document.getElementById('groupId');
  const nameEl  = document.getElementById('voterName');
  if(groupEl) groupEl.value = activeGroupId;
  if(nameEl)  nameEl.value  = user.name || '';
  renderCards();
}

function renderCards() {
  const stack = document.getElementById('cardStack');
  if(!stack) return;
  stack.innerHTML = '';
  const remaining = VOTE_DESTINATIONS.slice(currentCardIndex, currentCardIndex+3);
  if(remaining.length === 0) { showDoneState(); return; }
  [...remaining].reverse().forEach((dest,i) => {
    const isTop = i === remaining.length-1;
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
          <div class="v-card-tags">${dest.tags.map(t=>`<span class="v-card-tag">${t}</span>`).join('')}</div>
        </div>
        <div class="v-card-cost">💰 ${dest.cost}</div>
      </div>`;
    stack.appendChild(card);
    if(isTop) initDrag(card);
  });
  updateProgress();
}

function initDrag(card) {
  let startX=0, currentX=0, isDragging=false;
  card.addEventListener('mousedown', e => { isDragging=true; startX=e.clientX; card.style.transition='none'; });
  document.addEventListener('mousemove', e => {
    if(!isDragging) return;
    currentX = e.clientX - startX;
    card.style.transform = `translateX(${currentX}px) rotate(${currentX*0.04}deg)`;
    const like=card.querySelector('.like-stamp'), nope=card.querySelector('.nope-stamp');
    if(like) like.style.opacity = currentX>40 ? Math.min((currentX-40)/80,1) : 0;
    if(nope) nope.style.opacity = currentX<-40 ? Math.min((-currentX-40)/80,1) : 0;
  });
  document.addEventListener('mouseup', () => {
    if(!isDragging) return;
    isDragging = false;
    if(currentX>90)       animateCard(card,'love');
    else if(currentX<-90) animateCard(card,'skip');
    else { card.style.transition='transform 0.4s ease'; card.style.transform=''; }
    currentX = 0;
  });
  card.addEventListener('touchstart', e => { startX=e.touches[0].clientX; card.style.transition='none'; });
  card.addEventListener('touchmove', e => {
    currentX = e.touches[0].clientX - startX;
    card.style.transform = `translateX(${currentX}px) rotate(${currentX*0.04}deg)`;
    const like=card.querySelector('.like-stamp'), nope=card.querySelector('.nope-stamp');
    if(like) like.style.opacity = currentX>40 ? Math.min((currentX-40)/80,1) : 0;
    if(nope) nope.style.opacity = currentX<-40 ? Math.min((-currentX-40)/80,1) : 0;
  });
  card.addEventListener('touchend', () => {
    if(currentX>90)       animateCard(card,'love');
    else if(currentX<-90) animateCard(card,'skip');
    else { card.style.transition='transform 0.4s ease'; card.style.transform=''; }
    currentX = 0;
  });
}

function animateCard(card, direction) {
  const dest = VOTE_DESTINATIONS[currentCardIndex];
  card.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
  card.style.transform  = `translateX(${direction==='love'?900:-900}px) rotate(${direction==='love'?25:-25}deg)`;
  card.style.opacity    = '0';
  if(direction==='love' || direction==='maybe') {
    votedDestinations.push(dest.name);
    showToast(direction==='love' ? `❤️ ${dest.name} added!` : `⭐ ${dest.name} maybe!`);
  }
  currentCardIndex++;
  setTimeout(renderCards, 380);
}

function swipeCard(direction) {
  const stack   = document.getElementById('cardStack');
  if(!stack) return;
  const topCard = stack.lastElementChild;
  if(topCard && topCard.classList.contains('v-card')) animateCard(topCard, direction);
  else showDoneState();
}

function updateProgress() {
  const pct     = Math.round((currentCardIndex/VOTE_DESTINATIONS.length)*100);
  const fill    = document.getElementById('progressFill');
  const counter = document.getElementById('voteCounter');
  if(fill)    fill.style.width    = pct+'%';
  if(counter) counter.textContent = `${currentCardIndex} / ${VOTE_DESTINATIONS.length} voted`;
}

function showDoneState() {
  const stack=document.getElementById('cardStack'), done=document.getElementById('doneState'), actions=document.getElementById('voteActionsRow');
  if(stack)   stack.style.display   = 'none';
  if(done)    done.style.display    = 'block';
  if(actions) actions.style.display = 'none';
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
  if(el.classList.contains('selected')) selectedStyles.push(label);
  else selectedStyles = selectedStyles.filter(s => s!==label);
}

async function submitVote() {
  const user      = loadUser();
  const voterName = document.getElementById('voterName')?.value.trim() || user?.name;
  const groupId   = activeGroupId || document.getElementById('groupId')?.value.trim();
  const duration  = parseInt(document.getElementById('duration')?.value || '7');
  const month     = document.getElementById('month')?.value || 'December';
  if(!voterName) { showToast('Enter your name','error'); return; }
  if(!groupId)   { showToast('No group found','error'); return; }
  const preferences = {
    destinations: votedDestinations.length>0 ? votedDestinations : ['Jaipur','Goa','Kerala'],
    budget:       selectedBudget,
    travel_style: selectedStyles.length>0 ? selectedStyles : ['culture','food'],
    duration, month
  };
  try {
    const res  = await fetch(`${API}/vote/submit`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ group_id:groupId, user_name:voterName, preferences })
    });
    const data = await res.json();
    if(data.success) { showToast('Vote submitted! 🎉'); setTimeout(() => window.location.href='results.html', 1200); }
    else showToast(data.error||'Error submitting vote','error');
  } catch(e) { showToast('Cannot connect to server','error'); }
}

// ══════════════════════════════════════════════════════════════════════════
// RESULTS PAGE
// ══════════════════════════════════════════════════════════════════════════
let PackVoteMap = null;

async function initResultsPage() {
  if(!document.getElementById('winnerName')) return;
  const user = requireAuth();
  if(!user) return;
  const group = await fetchActiveGroup(user.user_id);
  if(!group) { loadDemoResults(); return; }
  try {
    const res  = await fetch(`${API}/vote/results/${group.group_id}`);
    const data = await res.json();
    if(data.error) { loadDemoResults(); return; }
    renderResults(data);
    const winner = data.consensus?.winner;
    if(winner) { await loadWeather(winner); await loadItinerary(winner, data.consensus); }
  } catch(e) { loadDemoResults(); }
}

function loadDemoResults() {
  renderResults({
    group_name:'Demo Group', total_votes:3,
    consensus:{
      winner:'Jaipur',
      top_destinations:[
        {destination:'Jaipur',percentage:100},{destination:'Goa',percentage:78},
        {destination:'Kerala',percentage:65},{destination:'Manali',percentage:50},{destination:'Udaipur',percentage:40}
      ],
      consensus_budget:'medium', avg_duration:7, consensus_month:'December',
      top_styles:['culture','food','adventure'], conflicts:[]
    },
    recommendations:[
      {destination:'Jaipur',match_percentage:95,description:'The Pink City',avg_cost_per_day:3500,tags:['history','culture']},
      {destination:'Udaipur',match_percentage:88,description:'City of Lakes',avg_cost_per_day:4000,tags:['romance','history']},
      {destination:'Jodhpur',match_percentage:82,description:'The Blue City',avg_cost_per_day:3000,tags:['history','culture']},
    ]
  });
  loadWeather('Jaipur');
  loadItinerary('Jaipur',{avg_duration:7,consensus_budget:'medium',top_styles:['culture'],consensus_month:'December'});
}

function renderResults(data) {
  const c = data.consensus;
  setText('winnerName', c.winner||'Your Destination');
  setText('winnerDesc', getDestDesc(c.winner));
  const bgImg = document.getElementById('winnerBgImg');
  if(bgImg) {
    bgImg.style.opacity='0'; bgImg.src=getDestImage(c.winner);
    bgImg.onload=() => { bgImg.style.transition='opacity 1.5s ease'; bgImg.style.opacity='1'; };
  }
  setText('statVoters', data.total_votes);
  setText('statDays',   (c.avg_duration||'—')+(c.avg_duration?'d':''));
  setText('statBudget', capitalize(c.consensus_budget));
  setText('statMonth',  c.consensus_month?.slice(0,3)||'—');
  const scoreList = document.getElementById('scoreList');
  if(scoreList && c.top_destinations) {
    scoreList.innerHTML = c.top_destinations.map((d,i) => `
      <div class="score-bar">
        <div class="score-label">${i===0?'🏆':'#'+(i+1)} ${d.destination}</div>
        <div class="score-track"><div class="score-fill" style="width:0%" data-pct="${d.percentage}"></div></div>
        <div class="score-pct">${d.percentage}%</div>
      </div>`).join('');
    setTimeout(() => { document.querySelectorAll('.score-fill').forEach(el => { el.style.width=el.dataset.pct+'%'; }); }, 400);
  }
  const recList = document.getElementById('recList');
  if(recList && data.recommendations) {
    recList.innerHTML = data.recommendations.map((r,i) => `
      <div class="rec-card">
        <div class="rec-rank ${i===0?'top':''}">${i===0?'🥇':i===1?'🥈':'🥉'}</div>
        <img src="${getDestImage(r.destination)}" style="width:56px;height:56px;border-radius:10px;object-fit:cover;flex-shrink:0;" alt="${r.destination}"/>
        <div class="rec-info">
          <div class="rec-name">${r.destination}</div>
          <div class="rec-desc">${r.description}</div>
          <div class="rec-meta"><span>₹${(r.avg_cost_per_day||0).toLocaleString()}/day</span><span>${(r.tags||[]).slice(0,2).join(' · ')}</span></div>
        </div>
        <div class="rec-match">${r.match_percentage}%</div>
      </div>`).join('');
  }
  if(c.conflicts?.length>0) {
    const section=document.getElementById('conflictSection'), list=document.getElementById('conflictList');
    if(section) section.style.display='block';
    if(list) list.innerHTML=c.conflicts.map(cf=>`<div class="conflict-alert"><span class="conflict-icon">${cf.severity==='high'?'🔴':'🟡'}</span><span class="conflict-text">${cf.message}</span></div>`).join('');
  }
  initMap(c.winner);
}

async function loadWeather(destination) {
  try {
    const res  = await fetch(`${API}/weather/${encodeURIComponent(destination)}`);
    const data = await res.json();
    setText('weatherTemp',     `${data.temperature_c}°C`);
    setText('weatherDesc',     data.description||'Clear skies');
    setText('weatherHumidity', `Humidity: ${data.humidity}%`);
    const forecastRow = document.getElementById('forecastRow');
    if(forecastRow && data.forecast?.length>0) {
      forecastRow.innerHTML = data.forecast.map(f => `
        <div class="forecast-day">
          <div class="date">${f.date}</div>
          <div class="temp">${f.max_temp}° / ${f.min_temp}°</div>
          <div style="font-size:0.72rem;color:var(--text-muted);margin-top:2px;">${(f.description||'').split(' ').slice(0,2).join(' ')}</div>
        </div>`).join('');
    }
  } catch(e) { setText('weatherDesc','Weather data unavailable'); }
}

async function loadItinerary(destination, consensus) {
  try {
    const res  = await fetch(`${API}/itinerary/generate`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
        destination, duration:consensus.avg_duration||7,
        budget:consensus.consensus_budget||'medium',
        travel_style:consensus.top_styles||['culture'],
        month:consensus.consensus_month||'December'
      })
    });
    const data = await res.json();
    if(data.itinerary) { renderCost(data.itinerary.estimated_cost); renderItinerary(data.itinerary); }
  } catch(e) { renderFallbackItinerary(destination); }
}

function renderCost(cost) {
  const grid = document.getElementById('costGrid');
  if(!grid || !cost?.per_person) return;
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
  if(!list) return;
  const days = itinerary.days||[];
  if(days.length===0) { renderFallbackItinerary(itinerary.destination); return; }
  list.innerHTML = days.map(day => `
    <div class="day-card">
      <div class="day-header" onclick="toggleDay(this)">
        <div class="day-number">D${day.day}</div>
        <div><div class="day-title">${day.title}</div><div style="font-size:0.8rem;color:var(--text-muted);">${(day.activities||[]).length} activities</div></div>
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
  renderItinerary({destination, days:[
    {day:1,title:'Arrival & Exploration',activities:[{name:'Check in & freshen up',type:'accommodation'},{name:'Evening walk',type:'sightseeing'},{name:'Welcome dinner',type:'food'}]},
    {day:2,title:'Main Attractions',activities:[{name:'Top historical sites',type:'sightseeing'},{name:'Local market',type:'shopping'},{name:'Street food lunch',type:'food'}]},
    {day:3,title:'Culture & Heritage',activities:[{name:'Museum visit',type:'culture'},{name:'Art gallery',type:'art'},{name:'Traditional dinner',type:'food'}]},
    {day:4,title:'Adventure Day',activities:[{name:'Guided tour',type:'tour'},{name:'Adventure activity',type:'adventure'},{name:'Rooftop dinner',type:'food'}]},
    {day:5,title:'Leisure & Departure',activities:[{name:'Morning at leisure',type:'relaxation'},{name:'Last minute shopping',type:'shopping'},{name:'Farewell dinner',type:'food'}]},
  ]});
}

function toggleDay(header) {
  header.classList.toggle('open');
  header.nextElementSibling.classList.toggle('open');
}

function initMap(destination) {
  if(!window.L) return;
  const mapEl = document.getElementById('map');
  if(!mapEl || PackVoteMap) return;
  const coords = getDestCoords(destination);
  PackVoteMap = L.map('map').setView(coords,11);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution:'© OpenStreetMap contributors'}).addTo(PackVoteMap);
  const icon = L.divIcon({html:`<div style="background:linear-gradient(135deg,#6c63ff,#ff6584);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 4px 16px rgba(108,99,255,0.5);border:3px solid white;">✈</div>`,className:'',iconSize:[40,40],iconAnchor:[20,20]});
  L.marker(coords,{icon}).addTo(PackVoteMap).bindPopup(`<b>${destination}</b><br>Your group's destination! 🎉`).openPopup();
}

function shareWhatsApp() {
  const winner = document.getElementById('winnerName')?.textContent||'our destination';
  window.open(`https://wa.me/?text=${encodeURIComponent(`🌍 Our group is going to *${winner}*!\nPlanned with PackVote ✈\nVote. Plan. Fly.`)}`, '_blank');
}
function copyLink() { navigator.clipboard.writeText(window.location.href); showToast('Link copied! 🔗'); }

// ══════════════════════════════════════════════════════════════════════════
// EXPENSES PAGE
// ══════════════════════════════════════════════════════════════════════════
let expGroupId='', expMembers=[], selectedCat='food', splitType='equal', expenseChart=null;

async function initExpensesPage() {
  if(!document.getElementById('expGroupId')) return;
  const user = requireAuth();
  if(!user) return;
  const group = await fetchActiveGroup(user.user_id);
  if(!group) { showToast('No group found. Create or join a group first.','error'); return; }
  const groupDetails = await fetchGroupDetails(group.group_id);
  if(!groupDetails) return;
  expMembers = groupDetails.members || [];
  const groupIdEl = document.getElementById('expGroupId');
  if(groupIdEl) groupIdEl.value = group.group_id;
  setupGroupDirect(group.group_id, expMembers);
}

function renderExpMembersList() {
  const list = document.getElementById('expMembersList');
  if(!list) return;
  list.innerHTML = expMembers.map(m => `
    <div class="member-check checked">
      <div class="member-avatar" style="width:20px;height:20px;font-size:0.65rem;">${m[0].toUpperCase()}</div>${m}
    </div>`).join('');
}

function setupGroupDirect(groupId, members) {
  expGroupId = groupId; expMembers = members;
  const setupEl=document.getElementById('groupSetup'), formEl=document.getElementById('addExpenseForm'), barEl=document.getElementById('groupInfoBar');
  if(setupEl) setupEl.style.display='none';
  if(formEl)  formEl.style.display='block';
  if(barEl)   barEl.style.display='flex';
  setText('activeGroupLabel', groupId);
  setText('activeMembersLabel', members.join(', '));
  const select = document.getElementById('expPaidBy');
  if(select) { select.innerHTML='<option value="">Select who paid</option>'+members.map(m=>`<option value="${m}">${m}</option>`).join(''); }
  renderSplitMembers(members);
  loadExpenses();
}

function renderSplitMembers(members) {
  const container = document.getElementById('splitMembers');
  if(!container) return;
  container.innerHTML = members.map(m => `
    <div class="member-check checked" onclick="toggleSplitMember(this)" data-member="${m}">
      <div class="member-avatar" style="width:20px;height:20px;font-size:0.65rem;">${m[0].toUpperCase()}</div>${m}
    </div>`).join('');
}

function toggleSplitMember(el) { el.classList.toggle('checked'); if(splitType==='custom') renderCustomSplitInputs(); }

function selectCat(el) { document.querySelectorAll('.cat-btn').forEach(b=>b.classList.remove('active')); el.classList.add('active'); selectedCat=el.dataset.cat; }

function setSplitType(type) {
  splitType=type;
  const equalEl=document.getElementById('splitEqual'), customEl=document.getElementById('splitCustom'), areaEl=document.getElementById('customSplitArea');
  if(equalEl)  equalEl.classList.toggle('selected', type==='equal');
  if(customEl) customEl.classList.toggle('selected', type==='custom');
  if(areaEl)   areaEl.style.display = type==='custom'?'block':'none';
  if(type==='custom') renderCustomSplitInputs();
}

function renderCustomSplitInputs() {
  const checked   = [...document.querySelectorAll('#splitMembers .member-check.checked')];
  const amount    = parseFloat(document.getElementById('expAmount')?.value)||0;
  const perPerson = checked.length>0 ? (amount/checked.length).toFixed(2) : 0;
  const container = document.getElementById('customSplitInputs');
  if(!container) return;
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
  const checked = [...document.querySelectorAll('#splitMembers .member-check.checked')].map(el=>el.dataset.member);
  if(!desc)                { showToast('Enter a description','error'); return; }
  if(!amount || amount<=0) { showToast('Enter a valid amount','error'); return; }
  if(!paidBy)              { showToast('Select who paid','error'); return; }
  if(checked.length===0)   { showToast('Select at least 1 member to split','error'); return; }
  let splitAmong = checked;
  if(splitType==='custom') {
    const customSplits={}; let total=0;
    for(const member of checked) { const val=parseFloat(document.getElementById(`custom_${member}`)?.value||0); customSplits[member]=val; total+=val; }
    if(Math.abs(total-amount)>0.5) { showToast(`Custom split total (₹${total}) must equal amount (₹${amount})`,'error'); return; }
    splitAmong = customSplits;
  }
  try {
    const res  = await fetch(`${API}/expenses/add`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({group_id:expGroupId, paid_by:paidBy, amount, description:desc, category:selectedCat, split_among:splitAmong, split_type:splitType})
    });
    const data = await res.json();
    if(data.success) {
      showToast(`₹${amount} added! 💰`);
      document.getElementById('expDesc').value=''; document.getElementById('expAmount').value='';
      loadExpenses();
    } else showToast(data.error||'Failed to add expense','error');
  } catch(e) { showToast('Cannot connect to server','error'); }
}

async function loadExpenses() {
  if(!expGroupId) return;
  try {
    const res  = await fetch(`${API}/expenses/${expGroupId}`);
    const data = await res.json();
    renderExpenses(data.expenses||[]); renderExpSummary(data.summary||{}); renderSettlements(data.settlements||[]);
  } catch(e) { showToast('Could not load expenses','error'); }
}

function renderExpenses(expenses) {
  const list = document.getElementById('expensesList');
  if(!list) return;
  if(expenses.length===0) { list.innerHTML=`<div class="empty-expenses"><span class="empty-emoji">🧾</span><p>No expenses yet — add your first one above!</p></div>`; return; }
  const catIcons={food:'🍜',transport:'🚗',hotel:'🏨',activities:'🎟️',shopping:'🛍️',other:'📦'};
  list.innerHTML=`<h3 style="font-family:var(--font-display);font-size:1rem;font-weight:700;margin-bottom:16px;">🧾 All Expenses (${expenses.length})</h3>`+
    expenses.slice().reverse().map(exp=>`
      <div class="expense-card">
        <div class="expense-icon cat-${exp.category}">${catIcons[exp.category]||'📦'}</div>
        <div class="expense-info"><div class="expense-name">${exp.description}</div><div class="expense-meta">Paid by <strong>${exp.paid_by}</strong> · Split: ${exp.split_among.join(', ')} · ${exp.date}</div></div>
        <div class="expense-amount">₹${exp.amount.toLocaleString()}</div>
        <button class="expense-delete" onclick="deleteExp('${exp.id}')">✕</button>
      </div>`).join('');
}

function renderExpSummary(summary) {
  if(!summary.total_spent) return;
  setText('statTotal',       '₹'+(summary.total_spent||0).toLocaleString());
  setText('statPerPerson',   '₹'+(summary.per_person_avg||0).toLocaleString());
  setText('statCount',       summary.total_expenses||0);
  setText('statSettlements', Object.keys(summary.balances||{}).length);
  const balancesCard=document.getElementById('balancesCard'), balancesList=document.getElementById('balancesList');
  if(summary.balances && Object.keys(summary.balances).length>0 && balancesCard && balancesList) {
    balancesCard.style.display='block';
    balancesList.innerHTML=Object.entries(summary.balances).map(([person,bal])=>`
      <div class="balance-row"><span>${person}</span><span class="${bal>=0?'balance-positive':'balance-negative'}">${bal>=0?'+':''}₹${Math.abs(bal).toLocaleString()} ${bal>=0?'(gets back)':'(owes)'}</span></div>`).join('');
  }
  if(summary.by_category && Object.keys(summary.by_category).length>0) {
    const chartCard=document.getElementById('chartCard');
    if(chartCard) { chartCard.style.display='block'; renderExpChart(summary.by_category); }
  }
  const shareCard=document.getElementById('shareCard'); if(shareCard) shareCard.style.display='block';
}

function renderSettlements(settlements) {
  const card=document.getElementById('settlementsCard'), list=document.getElementById('settlementsList');
  if(!card || !list) return;
  if(settlements.length===0) { card.style.display='none'; return; }
  card.style.display='block';
  list.innerHTML=settlements.map(s=>`
    <div class="settlement-card"><span class="settlement-from">${s.from}</span><span class="settlement-arrow">→ pays →</span><span class="settlement-to">${s.to}</span><span class="settlement-amount">₹${s.amount.toLocaleString()}</span></div>`).join('');
}

function renderExpChart(byCategory) {
  if(!window.Chart) return;
  const ctx=document.getElementById('expenseChart'); if(!ctx) return;
  const labels=Object.keys(byCategory), values=Object.values(byCategory);
  const colors=['#ff6b35','#6c63ff','#43e97b','#ffd700','#ff6584','#a0a0b8'];
  if(expenseChart) expenseChart.destroy();
  expenseChart=new Chart(ctx.getContext('2d'),{type:'doughnut',data:{labels,datasets:[{data:values,backgroundColor:colors.slice(0,labels.length),borderWidth:0,hoverOffset:8}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{position:'bottom',labels:{color:'#a0a0b8',font:{size:12},boxWidth:12,padding:16}},tooltip:{callbacks:{label:ctx=>` ₹${ctx.raw.toLocaleString()}`}}}}});
}

async function deleteExp(expenseId) {
  if(!confirm('Delete this expense?')) return;
  try {
    const res  = await fetch(`${API}/expenses/delete/${expGroupId}/${expenseId}`,{method:'DELETE'});
    const data = await res.json();
    if(data.success) { showToast('Expense deleted'); loadExpenses(); }
  } catch(e) { showToast('Could not delete','error'); }
}

function shareExpenses() {
  const total=document.getElementById('statTotal')?.textContent||'₹0', count=document.getElementById('statCount')?.textContent||'0';
  window.open(`https://wa.me/?text=${encodeURIComponent(`💰 *PackVote Expense Summary*\nGroup: ${expGroupId}\nTotal: ${total} across ${count} expenses\nSplit tracked with PackVote ✈`)}`, '_blank');
}

// ══════════════════════════════════════════════════════════════════════════
// PLANNER PAGE
// ══════════════════════════════════════════════════════════════════════════
let planGroupId='', planMembers=[], allTasks=[], activeFilter='all', activePerson='all';
const CAT_ICONS={documents:'📄',bookings:'🎫',packing:'🧳',activities:'🎯',other:'📦'};

async function initPlannerPage() {
  if(!document.getElementById('planGroupId')) return;
  const user = requireAuth();
  if(!user) return;
  const group = await fetchActiveGroup(user.user_id);
  if(!group) { showToast('No group found. Create or join a group first.','error'); return; }
  const groupDetails = await fetchGroupDetails(group.group_id);
  planMembers = groupDetails?.members || [];
  const planGroupEl = document.getElementById('planGroupId');
  if(planGroupEl) planGroupEl.value = group.group_id;
  planGroupId = group.group_id;
  populatePlannerAssignees();
  loadPlanner();
}

async function loadPlanner() {
  const groupId = document.getElementById('planGroupId')?.value.trim();
  if(!groupId) { showToast('Enter a group ID','error'); return; }
  planGroupId = groupId;
  try {
    const res  = await fetch(`${API}/planner/${groupId}`);
    const data = await res.json();
    allTasks   = data.tasks || [];
    const generateWrap=document.getElementById('generateWrap'), addTaskForm=document.getElementById('addTaskForm'), shareSection=document.getElementById('shareSection');
    if(generateWrap) generateWrap.style.display='block';
    if(addTaskForm)  addTaskForm.style.display='block';
    if(shareSection) shareSection.style.display='block';
    populatePlannerAssignees(); renderTasks(); updatePlannerStats(data.stats||{}); renderPersonFilters();
    showToast(`Planner loaded! ${allTasks.length} tasks 📋`);
  } catch(e) { showToast('Cannot connect to server','error'); }
}

function populatePlannerAssignees() {
  const select = document.getElementById('taskAssignee'); if(!select) return;
  select.innerHTML = '<option value="Unassigned">Unassigned</option>'+planMembers.map(m=>`<option value="${m}">${m}</option>`).join('');
}

async function generateTasks() {
  const destination=document.getElementById('planDestination')?.value.trim()||'your destination';
  const duration=parseInt(document.getElementById('planDuration')?.value)||7;
  if(!planGroupId) { showToast('Load planner first','error'); return; }
  if(allTasks.length>0 && !confirm('Add default tasks to existing list?')) return;
  try {
    const res  = await fetch(`${API}/planner/generate`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({group_id:planGroupId,destination,duration,members:planMembers})});
    const data = await res.json();
    allTasks=data.tasks||[]; renderTasks(); updatePlannerStats(data.stats||{}); renderPersonFilters();
    showToast(`✨ ${allTasks.length} tasks generated!`);
  } catch(e) { showToast('Cannot connect to server','error'); }
}

async function addTask() {
  const title=document.getElementById('taskTitle')?.value.trim();
  if(!title) { showToast('Enter a task title','error'); return; }
  try {
    const res  = await fetch(`${API}/planner/add`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({group_id:planGroupId,title,description:document.getElementById('taskDesc')?.value.trim(),category:document.getElementById('taskCategory')?.value,assigned_to:document.getElementById('taskAssignee')?.value,priority:document.getElementById('taskPriority')?.value,due_date:document.getElementById('taskDueDate')?.value})});
    const data = await res.json();
    if(data.success) {
      allTasks.push(data.task);
      document.getElementById('taskTitle').value=''; document.getElementById('taskDesc').value=''; document.getElementById('taskDueDate').value='';
      renderTasks(); refreshPlannerStats(); showToast('Task added! ✅');
    }
  } catch(e) { showToast('Cannot connect to server','error'); }
}

async function toggleTask(taskId) {
  try {
    const res  = await fetch(`${API}/planner/toggle/${planGroupId}/${taskId}`,{method:'PUT'});
    const data = await res.json();
    if(data.success) { const task=allTasks.find(t=>t.id===taskId); if(task) task.completed=data.completed; renderTasks(); refreshPlannerStats(); }
  } catch(e) { showToast('Cannot connect to server','error'); }
}

async function deleteTask(taskId) {
  if(!confirm('Delete this task?')) return;
  try {
    const res  = await fetch(`${API}/planner/delete/${planGroupId}/${taskId}`,{method:'DELETE'});
    const data = await res.json();
    if(data.success) { allTasks=allTasks.filter(t=>t.id!==taskId); renderTasks(); refreshPlannerStats(); showToast('Task deleted'); }
  } catch(e) { showToast('Cannot connect to server','error'); }
}

function renderTasks() {
  const list = document.getElementById('taskList'); if(!list) return;
  let filtered = allTasks;
  if(activeFilter!=='all') filtered=filtered.filter(t=>t.category===activeFilter);
  if(activePerson!=='all') filtered=filtered.filter(t=>t.assigned_to===activePerson);
  if(filtered.length===0) { list.innerHTML=`<div class="empty-tasks"><span class="empty-emoji">✅</span><p>${allTasks.length===0?'No tasks yet — generate or add tasks above!':'No tasks match this filter.'}</p></div>`; return; }
  const categories=activeFilter==='all'?['documents','bookings','packing','activities','other']:[activeFilter];
  let html='';
  for(const cat of categories) {
    const catTasks=filtered.filter(t=>t.category===cat); if(catTasks.length===0) continue;
    const done=catTasks.filter(t=>t.completed).length;
    html+=`<div class="task-category"><div class="task-category-header"><span class="task-category-icon">${CAT_ICONS[cat]||'📦'}</span><span class="task-category-title">${capitalize(cat)}</span><span class="task-category-progress">${done}/${catTasks.length}</span></div>
      ${catTasks.map(task=>{
        const pClass=`priority-${task.priority}`, pLabel=task.priority==='high'?'🔴 High':task.priority==='medium'?'🟡 Medium':'🟢 Low';
        return `<div class="task-item ${task.completed?'completed':''}" id="task_${task.id}"><div class="task-check" onclick="toggleTask('${task.id}')">${task.completed?'✓':''}</div><div class="task-content"><div class="task-title">${task.title}</div>${task.description?`<div class="task-desc">${task.description}</div>`:''}<div class="task-meta"><span class="task-assignee">👤 ${task.assigned_to}</span><span class="task-priority ${pClass}">${pLabel}</span>${task.due_date?`<span class="task-due">📅 ${task.due_date}</span>`:''}</div></div><button class="task-delete" onclick="deleteTask('${task.id}')">✕</button></div>`;
      }).join('')}</div>`;
  }
  list.innerHTML=html; updatePlannerCounts();
}

function filterTasks(filter,btn) { activeFilter=filter; activePerson='all'; document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active')); btn.classList.add('active'); document.querySelectorAll('.person-filter-btn').forEach(b=>b.classList.remove('active')); renderTasks(); }
function filterByPerson(person,btn) { activePerson=person; activeFilter='all'; document.querySelectorAll('.filter-btn,.person-filter-btn').forEach(b=>b.classList.remove('active')); btn.classList.add('active'); renderTasks(); }

async function refreshPlannerStats() {
  try { const res=await fetch(`${API}/planner/${planGroupId}`); const data=await res.json(); updatePlannerStats(data.stats||{}); renderPersonFilters(); } catch(e) {}
}

function updatePlannerStats(stats) {
  const pct=stats.percentage||0;
  setText('progressPct',pct+'%'); setText('progressLabel',`${stats.completed||0} of ${stats.total||0} tasks done`);
  const mainFill=document.getElementById('mainProgressFill'); if(mainFill) mainFill.style.width=pct+'%';
  const section=document.getElementById('personStatsSection'), psDiv=document.getElementById('personStats');
  if(stats.by_person && Object.keys(stats.by_person).length>0 && section && psDiv) {
    section.style.display='block';
    psDiv.innerHTML=Object.entries(stats.by_person).map(([person,data])=>{
      const pct=data.total>0?Math.round((data.completed/data.total)*100):0;
      return `<div class="person-stat"><span style="font-size:0.85rem;">${person}</span><div class="person-stat-bar"><div class="person-stat-fill" style="width:${pct}%"></div></div><span style="font-size:0.78rem;color:var(--text-muted);">${data.completed}/${data.total}</span></div>`;
    }).join('');
  }
  updatePlannerCounts();
}

function updatePlannerCounts() {
  setText('countAll',allTasks.length);
  ['documents','bookings','packing','activities','other'].forEach(cat=>{const el=document.getElementById('count'+capitalize(cat)); if(el) el.textContent=allTasks.filter(t=>t.category===cat).length;});
}

function renderPersonFilters() {
  const container=document.getElementById('personFilters'); if(!container) return;
  const people=[...new Set(allTasks.map(t=>t.assigned_to))];
  if(people.length===0) { container.innerHTML='<p style="font-size:0.82rem;color:var(--text-muted);">No tasks assigned yet</p>'; return; }
  container.innerHTML=`<button class="filter-btn person-filter-btn active" onclick="filterByPerson('all',this)">👥 Everyone <span class="filter-count">${allTasks.length}</span></button>`+
    people.map(p=>`<button class="filter-btn person-filter-btn" onclick="filterByPerson('${p}',this)">👤 ${p} <span class="filter-count">${allTasks.filter(t=>t.assigned_to===p).length}</span></button>`).join('');
}

function sharePlanner() {
  const done=allTasks.filter(t=>t.completed).length, total=allTasks.length;
  const pending=allTasks.filter(t=>!t.completed).slice(0,5).map(t=>`• ${t.title} (${t.assigned_to})`).join('\n');
  window.open(`https://wa.me/?text=${encodeURIComponent(`✅ *PackVote Trip Planner*\nProgress: ${done}/${total} tasks done\n\n*Pending:*\n${pending}\n\nPlanned with PackVote ✈`)}`, '_blank');
}

// ══════════════════════════════════════════════════════════════════════════
// AUTO INIT
// ══════════════════════════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  initIndexPage();
  initVotePage();
  initResultsPage();
  initExpensesPage();
  initPlannerPage();

  const memberInput=document.getElementById('memberInput');
  if(memberInput) memberInput.addEventListener('keypress',e=>{if(e.key==='Enter')addMember();});
  const taskTitleInput=document.getElementById('taskTitle');
  if(taskTitleInput) taskTitleInput.addEventListener('keypress',e=>{if(e.key==='Enter')addTask();});

  const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.style.opacity='1';entry.target.style.transform='translateY(0)';}});},{threshold:0.1});
  document.querySelectorAll('.how-step,.dest-img-card,.feature-card').forEach(el=>{el.style.opacity='0';el.style.transform='translateY(30px)';el.style.transition='opacity 0.6s ease, transform 0.6s ease';observer.observe(el);});
});