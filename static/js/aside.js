$(function() {

  $('#menuBtn').on('click', function(){
    $('.sideBar').toggleClass('open');
    $('.menu').toggleClass('active');
    $('body').css('overflow', 'hidden');
  });

  // Menu Close
  $('.menuClose').on('click', function(){
    $('.sideBar').toggleClass('open');
    $('.menu').removeClass('active');
    $('body').css('overflow', 'visible');
  });

  $(".sideBar").click(function (e) {
    $('.sideBar').toggleClass('open');
    $('.menu').removeClass('active');
    $('body').css('overflow', 'visible');
  });

  $(".menu").click(function (e) {
  e.stopPropagation();
});

});