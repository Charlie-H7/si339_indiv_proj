document.querySelectorAll('img').forEach(img => {
    console.log("fetching image")
    img.onerror = function () {
        this.onerror = null;
        this.src = "images/default_image.jpg";
        this.alt = "default image";
        // <!--
        // onerror="this.onerror=null; this.src='../images/default_image.jpg';"
        // -->
        // this.style.display = "none"
    }
    
  });