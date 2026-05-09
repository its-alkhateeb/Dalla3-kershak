// Profile picture preview
document.getElementById('profilePic').addEventListener('change', function () {
  const file = this.files[0];
  const circle = document.getElementById('profileCircle');
  const preview = document.getElementById('profilePreview');

  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      preview.src = e.target.result;
      circle.classList.add('has-image');
    };
    reader.readAsDataURL(file);
  } else {
    preview.src = '';
    circle.classList.remove('has-image');
  }
});

function togglePass(id, btn) {
  const input = document.getElementById(id);
  const isText = input.type === 'text';
  input.type = isText ? 'password' : 'text';
  btn.style.color = isText ? '#b8a080' : '#b8860b';
}

function checkStrength(val) {
  let score = 0;
  if (val.length >= 8) score++;
  if (/[A-Z]/.test(val)) score++;
  if (/[0-9]/.test(val)) score++;
  if (/[^A-Za-z0-9]/.test(val)) score++;

  const colors = ['#e0c89a', '#e24b4a', '#ef9f27', '#b8860b', '#3b6d11'];
  const labels = ['', 'Weak', 'Fair', 'Good', 'Strong'];

  for (let i = 1; i <= 4; i++) {
    document.getElementById('b' + i).style.background =
      i <= score ? colors[score] : '#e0c89a';
  }

  document.getElementById('strengthLabel').textContent =
    val.length ? labels[score] : '';
}