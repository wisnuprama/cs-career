
const openTab = (event, idTab) => {
  console.log("open tab " + idTab);
  let i;
  // change button
  const tabButton = $('.tab-button');
  const active = 'tab-button-active';
  for(i=0; i < tabButton.length; i++){
    $(tabButton[i]).removeClass(active)
  }
  $(event.currentTarget).addClass(active);

  // change tab content
  const tabContent = $('.tab-content');
  const inactive = 'none';
  for(i=0; i < tabContent.length; i++){
    $(tabContent[i]).css('display',inactive);
  }
  $('\#' + idTab).css('display', 'flex');
};


