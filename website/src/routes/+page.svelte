<script>
  let page1Text = "block";
  let page2Text = "none";
  let page3Text = "none";
  let startPage = "block";
  let finalPage = "none";
  let showDownloadButtons = "none";
  let moreInfoButton = "none";
  let continueButton = "block";
  let readAgainButton = "none";
  let desktopDownloadButton = "none";
  let mobileDownloadButton = "none";
  let mobileDownloadLinks = "none";

  let enterButtonBgColor = "#ffffff";

  let mouseX;
  let mouseY;

  function emulateButtonHover(element, time) {
    document.getElementById(element).style.backgroundColor = "#eeeeee";
    setTimeout(() => {
      document.getElementById(element).style.backgroundColor = "#ffffffd0";
    }, time);
  }

  function enterKey() {
    if (page1Text == "block" && page2Text == "none" && page3Text == "none") {
      emulateButtonHover("enterButton", 200);
      page1Text = "none";
      page2Text = "block";
      page3Text = "none";
    } else if (
      page1Text == "none" &&
      page2Text == "block" &&
      page3Text == "none"
    ) {
      emulateButtonHover("moreInfoButton", 100);

      page1Text = "none";
      page2Text = "none";
      page3Text = "block";
      moreInfoButton = "block";
      continueButton = "none";
    } else if (
      page1Text == "none" &&
      page2Text == "none" &&
      page3Text == "block"
    ) {
      emulateButtonHover("readAgainButton", 100);

      page1Text = "none";
      page2Text = "none";
      page3Text = "none";
      finalPage = "flex";
      startPage = "none";
      readAgainButton = "block";
      moreInfoButton = "none";
    } else if (readAgainButton == "block") {
      emulateButtonHover("enterButton", 100);

      page1Text = "block";
      page2Text = "none";
      page3Text = "none";
      finalPage = "none";
      startPage = "block";
      continueButton = "block";
      readAgainButton = "none";
      moreInfoButton = "none";
    }
  }

  function downloadKey() {
    showDownloadButtons = "flex";
    function getMousePosition(event) {
      mouseX = event.clientX;
      mouseY = event.clientY;
    }
    document.addEventListener("mousemove", getMousePosition, { once: true });
  }

  function stopDownloadKey() {
    showDownloadButtons = "none";
    function getMousePosition(event) {
      mouseX = event.clientX;
      mouseY = event.clientY;
    }
    document.removeEventListener("mousemove", getMousePosition);
  }

  function downloadButton() {
    showDownloadButtons = "flex";
  }

  var down = false;
  document.addEventListener(
    "keydown",
    function (e) {
      if (down) return;
      down = true;
      switch (e.keyCode) {
        case 32:
          enterKey();
          break;
        case 68:
          downloadKey();
          break;
      }
    },
    false
  );

  document.addEventListener(
    "keyup",
    function (e) {
      down = false;
      switch (e.keyCode) {
        case 68:
          stopDownloadKey();
          break;
      }
    },
    false
  );

  let enterButtonPrefix = "";
  let moreInfoButtonPrefix = "";
  let readAgainButtonPrefix = "";

  function buttonPrefixesCorrect() {
    if (window.innerWidth <= 800) {
      enterButtonPrefix = "";
      moreInfoButtonPrefix = "";
      readAgainButtonPrefix = "";
      mobileDownloadButton = "block";
      desktopDownloadButton = "none";
    } else {
      enterButtonPrefix = "space to";
      moreInfoButtonPrefix = "space for";
      readAgainButtonPrefix = "space to";
      mobileDownloadButton = "none";
      desktopDownloadButton = "block";
    }
  }
  buttonPrefixesCorrect();
</script>

<main>
  <div id="heroImageCrop">
    <img
      src="moment hero.png"
      alt=""
      style="display: {startPage};"
      id="heroImage"
    />
  </div>

  <div id="finalImageCrop">
    <img
      src="final hero.jpg"
      alt=""
      height="450px"
      style="display: {finalPage};"
      id="finalImage"
    />
  </div>
  <div id="textDiv">
    <center>
      <p style="display: {page1Text};" id="firstText">
        <b>moment</b> is a minimalist (.txt) micro blogging platform built for the
        terminal
      </p>
      <p style="display: {page2Text};">
        create an account and start posting to your own lightweight .txt url
        within seconds!
      </p>
      <p style="display: {page3Text};">
        most personal blogs are filled with gibberish and face their timely
        death when their user doesn’t care enough for it. <br /> <br /> the terminal
        interface that moment provides you encourages you to cut the crap and helps
        you get your thoughts out to the internet.
      </p>
    </center>
    <div id="finalPageDiv" style="display: {finalPage};">
      <p id="leftText">
        its simplicity is an effort to make it as low in resources as possible,
        thus making it run faster, use less bandwidth, leave 0 carbon footprint
        and overall be better for a person’s mental health
      </p>
      <p id="rightText">
        made by <a href="https://adithya.zip/" target="_blank">adithya</a>
        <br />
        <a href="https://ko-fi.com/adithyasource" target="_blank"
          >buy me a coffee</a
        > <br />
        <a href="https://github.com/adithyasource/moment" target="_blank"
          >source code</a
        >
      </p>
    </div>
  </div>

  <div id="buttonsContainer">
    <a href="/" on:click|preventDefault={enterKey}>
      <div
        class="buttons"
        id="enterButton"
        style="display: {continueButton}; background-color: {enterButtonBgColor}"
      >
        {enterButtonPrefix} continue
      </div>
      <div
        class="buttons"
        id="moreInfoButton"
        style="display: {moreInfoButton};"
      >
        {moreInfoButtonPrefix} more info
      </div>
      <div
        class="buttons"
        style="display: {readAgainButton}; "
        id="readAgainButton"
      >
        {readAgainButtonPrefix} read again
      </div>
    </a>
    <div id="downloadPrompt" style="display: {desktopDownloadButton};">
      hold d to download
    </div>
    <div style="display: {mobileDownloadButton};">
      <a
        href="/"
        on:click|preventDefault={() => {
          if (mobileDownloadLinks == "flex") {
            mobileDownloadLinks = "none";
          } else {
            mobileDownloadLinks = "flex";
          }
        }}
      >
        <div class="buttons" id="downloadPromptMobile">download</div>
      </a>
      <div id="downloadBoxMobile" style="display: {mobileDownloadLinks};">
        <div />
        <a
          href="https://github.com/adithyasource/moment/releases/download/1.0.0/moment.1.0.0.msi"
          target="_blank"
        >
          <div class="buttons">.msi installer</div>
        </a>
        <a
          href="https://github.com/adithyasource/moment/releases/download/1.0.0/moment.1.0.0.exe"
          target="_blank"
        >
          <div class="buttons">.exe portable</div>
        </a>
      </div>
    </div>
  </div>

  <div
    id="downloadButtons"
    style="display: {showDownloadButtons}; position:absolute; top: {mouseY -
      10}px; left:{mouseX + -135}px"
  >
    <div id="downloadBox" />
    <a
      href="https://github.com/adithyasource/moment/releases/download/1.0.0/moment.1.0.0.msi"
      target="_blank"
    >
      <div class="buttons">.msi installer</div>
    </a>
    <a
      href="https://github.com/adithyasource/moment/releases/download/1.0.0/moment.1.0.0.exe"
      target="_blank"
    >
      <div class="buttons">.exe portable</div>
    </a>
    <img src="decal.svg" alt="" id="decalImage" />
  </div>
</main>

<svelte:window on:resize={buttonPrefixesCorrect} />

<style>
  @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap");

  * {
    font-family: "IBM Plex Mono", monospace;
    font-size: 14px;
  }

  :global(html) {
    background-color: #ffffff;
  }

  main {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding-top: 4%;
  }

  p {
    width: 700px;
    opacity: 0;
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
  }

  a {
    color: inherit;
  }

  #buttonsContainer a,
  #downloadButtons a {
    text-decoration: none;
  }

  #buttonsContainer {
    display: flex;
    gap: 100px;
    align-items: center;
    opacity: 0;
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
    animation-delay: 1.3s;
    padding-top: 2vh;
  }

  #finalPageDiv {
    display: flex;
    width: 700px;
    opacity: 0;
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
    animation-delay: 0.6s;
  }

  #firstText {
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
    animation-delay: 0.6s;
  }

  #rightText {
    text-align: right;
  }

  #rightText a {
    cursor: pointer;
  }

  #downloadButtons {
    color: #ff0000;
    display: flex;
    gap: 60px;
  }

  #downloadBox {
    position: absolute;
    width: 390px;
    height: 100px;
    left: -30px;
    opacity: 1;
    background-color: #ffffff69;
    top: -17px;
    outline: 1px solid #000;
    backdrop-filter: blur(10px);
  }

  #downloadBoxMobile {
    color: #ff0000;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  #decalImage {
    position: absolute;
    top: 50px;
    width: 100%;
  }

  @keyframes fadeInFromUp {
    from {
      opacity: 0;
      transform: translate(0, -10px);
    }
    to {
      opacity: 1;
      transform: translate(0, 0px);
    }
  }

  #heroImage {
    opacity: 0;
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
    height: 50vh;
  }

  #finalImage {
    opacity: 0;
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
  }

  #textDiv {
    opacity: 0;
    animation: fadeInFromUp ease 1s;
    animation-iteration-count: 1;
    animation-fill-mode: forwards;
    animation-delay: 0.6s;
    padding-top: 2vh;
    height: 15vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #downloadPrompt {
    color: #838383;
  }

  #downloadPromptMobile {
    color: #000;
  }

  .buttons {
    padding: 10px;
    background-color: #ffffffd0;
    -webkit-border-radius: 8px;
    -moz-border-radius: 8px;
    -khtml-border-radius: 8px;
    border-radius: 8px;
    outline: 1.5px solid #242424;
    width: max-content;
    backdrop-filter: blur(10px);
    transition: background-color 0.2s;
  }

  .buttons:hover {
    background-color: #eeeeee !important;
  }

  @media only screen and (max-width: 800px) {
    #heroImage,
    #finalImage {
      height: auto;
      width: 130%;
    }

    #finalImageCrop {
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 90%;
    }
    #heroImageCrop {
      overflow: hidden;
      width: 90%;
    }
    #buttonsContainer {
      gap: 40px;
      align-items: start;
      padding-top: 30px;
      padding-bottom: 80px;
    }
    p {
      width: 80%;
    }
    #finalPageDiv {
      flex-direction: column;
      width: 90%;
      justify-content: center;
      align-items: center;
    }
    #leftText,
    #rightText {
      text-align: center;
    }

    #textDiv {
      height: auto;
      padding-top: 30px;
    }
  }

  :global(body) {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }
</style>
