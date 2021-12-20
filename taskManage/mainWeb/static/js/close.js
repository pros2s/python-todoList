const close = document.querySelectorAll('#closeBtn'),
      list = document.querySelector('#taskList');

const closeTask = function () {
    this.parentElement.remove();
}
close.forEach(cross => cross.addEventListener('click', closeTask));