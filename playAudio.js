(function() {
    var audio = document.createElement('audio');
    audio.src = "{{AUDIO_SRC}}";
    audio.autoplay = true;
    audio.loop = false;
    document.body.appendChild(audio);
})();
