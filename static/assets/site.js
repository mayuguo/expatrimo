(function(){
  var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
  if(b&&n)b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
  // blog filter + search
  var list=document.getElementById('list');
  if(list){
    var cards=[].slice.call(list.querySelectorAll('.card')),chips=[].slice.call(document.querySelectorAll('.chip')),q=document.getElementById('q'),cnt=document.getElementById('count');
    var cat=(new URLSearchParams(location.search)).get('cat')||'';
    function norm(s){return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')}
    function apply(){
      var t=norm(q.value.trim()),k=0;
      cards.forEach(function(c){var ok=(!cat||c.dataset.cats.split('|').indexOf(cat)>=0)&&(!t||norm(c.dataset.text).indexOf(t)>=0);c.hidden=!ok;if(ok)k++});
      chips.forEach(function(ch){ch.setAttribute('aria-pressed',ch.dataset.cat===cat)});
      cnt.textContent=k+' article'+(k>1?'s':'');
    }
    chips.forEach(function(ch){ch.addEventListener('click',function(){cat=ch.dataset.cat;try{history.replaceState(null,'',cat?'?cat='+cat:location.pathname)}catch(e){}apply()})});
    q.addEventListener('input',apply);apply();
  }
  // contact form -> mailto
  var f=document.getElementById('contact-form');
  if(f)f.addEventListener('submit',function(e){
    e.preventDefault();var d=new FormData(f);
    var body='Nom : '+d.get('nom')+'\nEmail : '+d.get('email')+'\nPays de résidence : '+d.get('pays')+'\nSujet : '+d.get('sujet')+'\n\n'+d.get('message');
    var to=f.querySelector('a[href^="mailto:"]').getAttribute('href').slice(7);
    location.href='mailto:'+to+'?subject='+encodeURIComponent('Demande de mise en relation : '+d.get('sujet'))+'&body='+encodeURIComponent(body);
  });
})();
