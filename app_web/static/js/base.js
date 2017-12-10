const URL = {
  'status': {
    'GET': '/api/status/get/',
    'POST': '/api/status/post/',
    'DELETE': '/api/status/delete/',
  },
  'profile': {},
  'friend': {},
};

const canLoadPage = () => {
  return $('#timeline').length > 10;
};

const WINDOW = $(window);
let progress = false;
WINDOW.scroll(() => {
  console.log(progress)
  if (WINDOW.scrollTop() + WINDOW.height() > $(document).height() - 10 && !progress && canLoadPage()) {
    progress = true;
    $.ajax({
      method: 'GET',
      url: URL.status.GET,
      data: {

      }
    })
  }

});


const deleteStatus = (id) => {

  const statusId = id.split('-')[1];
  const csrfToken = $('[name=csrfmiddlewaretoken]').val();
  $.ajax({
    method: 'DELETE',
    headers: {
      'X-CSRFToken': csrfToken,
    },
    url: URL.status.DELETE,
    data: {
      'id': statusId,
    },
    success: (response) => {
      $('#' + id).remove();
    },
    error: (response) => {

    },
  });


};

const openTab = (event, idTab) => {
  console.log("open tab " + idTab);
  let i;
  // change button
  const tabButton = $('.tab-button');
  const active = 'tab-button-active';
  for (i = 0; i < tabButton.length; i++) {
    $(tabButton[i]).removeClass(active)
  }
  $(event.currentTarget).addClass(active);

  // change tab content
  const tabContent = $('.tab-content');
  const inactive = 'none';
  for (i = 0; i < tabContent.length; i++) {
    $(tabContent[i]).css('display', inactive);
  }
  $('\#' + idTab).css('display', 'flex');
};

const calculateChar = () => {

};

$(document).ready(() => {

  // BIND CLICK: Button kirim status
  $('#submit-post').on('click', (event) => {
    const statusElem = $('#status-textarea');
    const content = statusElem.val();

    const csrfToken = $('[name=csrfmiddlewaretoken]').val();

    $.ajax({
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
      },
      url: URL.status.POST,
      data: {
        'content': content,
      },
      success: (response) => {
        //add to top of timeline
        const status = response.result;
        html = '<div class="status">\n' +
            '     <div class="user-dp">\n' +
            '       <img src="/static/img/user_dummy.png">\n' +
            '     </div>\n' +
            '     <div class="status-content">\n' +
            '       <span>\n' +
            '         <h3>' + status.user.first_name + '</h3>\n' +
            '         <p>' + status.user.username + '</p>\n' +
            '       </span>\n' +
            '         <p>' + status.content + '</p>\n' +
            '      </div>\n' +
            '      <div class="right-status">' +
            '        <span class="status-date">\n' + status.created_at + '</span>\n' +
            '        <button class="fa fa-trash-o trash" aria-hidden="true"></button>\n' +
            '      </div>\n' +
            ' </div>';

        $('#timeline').prepend(html);
        // change latest status
        $('#latest-status-content').text(status.content);
        // increament the numbers of status
        const num = $('#stat-status-number');
        num.text(
            parseInt(num.text()) + 1
        );
        // empty the textarea
        statusElem.val('');
      },
      error: () => {

      },
    });

    event.preventDefault();
  })

});
