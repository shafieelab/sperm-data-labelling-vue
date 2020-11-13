<template>
  <div>
    <footer class="Footer" id="contact">
      <div class="Container Footer-container">
        <div class="Container--default">
          <a
            aria-label=""
            class="footer__logo"
            href="http://shafieelab.bwh.harvard.edu"
            target="_blank"
          >
            <img
              alt="logo"
              height="39"
              src="./assets/logo_white.png"
              width="200"
            />
          </a>
          <div
            class="Footer-top"
            itemscope=""
            itemtype="http://schema.org/Organization"
          ></div>
          <div class="Footer-information">
            <div class="Footer-information-left">
              <!--              <nav class="Footer-menu">-->
              <!--                <ul class="Menu">-->
              <!--                  <li-->
              <!--                    class="Menu-item Menu-item&#45;&#45;type-aboutUs Menu-item&#45;&#45;object-aboutUs"-->
              <!--                  >-->
              <!--                    <router-link exact to="/positions">-->
              <!--                      Positions-->
              <!--                    </router-link>-->
              <!--                  </li>-->
              <!--                  <li-->
              <!--                    class="Menu-item Menu-item&#45;&#45;type-aboutUs Menu-item&#45;&#45;object-aboutUs"-->
              <!--                  >-->
              <!--                    &lt;!&ndash;<router-link exact to="/research">&ndash;&gt;-->
              <!--                    &lt;!&ndash;Research&ndash;&gt;-->
              <!--                    &lt;!&ndash;</router-link>&ndash;&gt;-->
              <!--                  </li>-->
              <!--                  <li-->
              <!--                    class="Menu-item Menu-item&#45;&#45;type-aboutUs Menu-item&#45;&#45;object-aboutUs"-->
              <!--                  >-->
              <!--                    <router-link exact to="/Publications">-->
              <!--                      Publications-->
              <!--                    </router-link>-->
              <!--                  </li>-->

              <!--                  <li-->
              <!--                    class="Menu-item Menu-item&#45;&#45;type-aboutUs Menu-item&#45;&#45;object-aboutUs"-->
              <!--                  >-->
              <!--                    <router-link exact to="/people">-->
              <!--                      People-->
              <!--                    </router-link>-->
              <!--                  </li>-->

              <!--                  <li-->
              <!--                    class="Menu-item Menu-item&#45;&#45;type-aboutUs Menu-item&#45;&#45;object-aboutUs"-->
              <!--                  >-->
              <!--                    <router-link exact to="/contact">-->
              <!--                      Contact Us-->
              <!--                    </router-link>-->
              <!--                  </li>-->
              <!--                </ul>-->
              <!--              </nav>-->
              <div class="Footer-copyright">
                Copyright © 2020 Shafiee Laboratory | All rights reserved
              </div>
            </div>
            <div class="Footer-information-right">
              <!--<p><a href="https://hemanthkandula.com" target="_blank">designed by  </a></p>-->
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>
<script>
export default {
  name: "AppFooter"
};
</script>
<style scoped>
@import "./assets/css/custom.css";

a {
  text-decoration: none;
}

@media all {
  * {
    -webkit-tap-highlight-color: transparent;
  }
  footer,
  nav {
    display: block;
  }
  a {
    background-color: transparent;
  }
  a:active,
  a:hover {
    outline: 0;
  }
  .Container:after,
  .Footer-information:after,
  .Footer-top:after,
  .Footer:after {
    content: "";
    display: table;
    clear: both;
  }
  .Container {
    max-width: 75rem;
    margin-left: auto;
    margin-right: auto;
  }
  .Container:after {
    content: " ";
    display: block;
    clear: both;
  }
  *,
  :after,
  :before {
    box-sizing: border-box;
  }
  .Container {
    z-index: 10;
  }
  @media (max-width: 78rem) {
    .Container {
      margin-right: 1.5rem;
      margin-left: 1.5rem;
    }
  }
  @media (max-width: 56.25rem) {
    .Container {
      margin-right: 1rem;
      margin-left: 1rem;
    }
  }
  .Container--default {
    width: 100%;
    float: left;
    padding-left: 0.83333%;
    padding-right: 0.83333%;
  }
  .Footer {
    color: #ccc;
    background-color: #242424;
  }
  .Footer-container a {
    text-decoration: none;
  }
  .Footer-container h3 {
    margin: 0 0 0.75rem;
    color: #666;
    font-size: 11px;
    font-weight: 600;
    line-height: 1;
    text-transform: uppercase;
  }
  .Footer-top a {
    color: #ccc !important;
  }
  .Footer-top {
    padding-top: 0.375rem;
  }
  @media (min-width: 48rem) {
    .Footer-container h3 {
      margin: 0 0 1rem;
      font-size: 12px;
    }
    .Footer-top {
      padding-top: 4.625rem;
    }
  }
  @media (min-width: 56.3125rem) {
    .Footer-top {
      padding-bottom: 3.75rem;
    }
  }
  .Footer-top a {
    font-weight: 300 !important;
  }
  .no-touchevents .Footer-top a:hover {
    color: #fff;
  }
  .Footer-address,
  .Footer-contact {
    padding: 1.75rem 0.83333% 1.25rem;
    font-size: 13px;
    font-weight: 100;
    line-height: 21px;
    letter-spacing: 1px;
    width: 50%;
    float: left;
  }
  @media (min-width: 48rem) {
    .Footer-address,
    .Footer-contact {
      padding: 0;
      font-size: 15px;
      line-height: 21px;
    }
  }
  @media (min-width: 56.25rem) {
    .Footer-address,
    .Footer-contact {
      width: 33.33333%;
      padding: 0;
      font-size: 16px;
      line-height: 24px;
    }
  }
  @media (min-width: 48rem) and (max-width: 56.25rem) {
    .Footer-address,
    .Footer-contact {
      padding-bottom: 2.25rem;
    }
  }
  @media screen and (max-width: 35.4375rem) {
    .Footer-address,
    .Footer-contact {
      width: 100%;
      border-bottom: 0.0625rem solid #2f2f2f;
    }
  }
  .Footer-contact {
    padding-left: 0;
  }
  .Footer-address {
    padding-right: 0;
  }
  .Footer-contact-title {
    display: inline-block;
    width: 4.6875rem;
  }
  @media (min-width: 48rem) {
    .Footer-contact-title {
      width: 5.625rem;
    }
  }
  .Footer-social {
    padding: 24px 0.83333%;
    text-align: center;
    width: 100%;
    float: left;
  }
  @media (min-width: 35.5rem) and (max-width: 56.1875rem) {
    .Footer-social {
      border-top: 0.0625rem solid #2f2f2f;
    }
  }
  @media (min-width: 30rem) {
    .Footer-social {
      padding: 24px 0;
    }
  }
  @media (min-width: 56.25rem) {
    .Footer-social {
      width: 33.33333%;
      padding: 0;
      text-align: right;
    }
  }
  .Footer-social .Icon {
    margin: 0 10px;
    font-size: 2.625rem;
  }
  .Footer-social .Icon:first-child {
    margin-left: 0;
  }
  .Footer-social .Icon:last-child {
    margin-right: 0;
  }
  @media (min-width: 56.3125rem) {
    .Footer-social .Icon {
      font-size: 2.25rem;
    }
  }
  .Footer-information {
    padding-top: 0;
    padding-bottom: 3.125rem;
    border-top: none;
    text-align: center;
  }
  @media (min-width: 48rem) {
    .Footer-information {
      padding: 1rem 0 1.5rem;
      color: #666;
      border-top: 0.0625rem solid #2f2f2f;
      text-align: left;
    }
  }
  .Footer-information a {
    color: #ccc !important;
    font-weight: 300 !important;
  }
  .no-touchevents .Footer-information a:hover {
    color: #254e70;
  }
  .Footer-information-left {
    width: 100%;
    float: left;
  }
  @media (min-width: 48rem) {
    .Footer-information-left {
      width: 50%;
    }
  }
  .Footer-information-right {
    text-align: center;
    width: 100%;
    float: left;
  }
  .Footer-menu {
    margin: 0 0 1.25rem;
  }
  @media (min-width: 48rem) {
    .Footer-information-right {
      width: 50%;
      text-align: right;
    }
    .Footer-menu {
      margin: 0;
    }
  }
  .Footer-menu .Menu {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .Footer-menu .Menu .Menu-item {
    display: inline-block;
    font-size: 0.6875rem;
  }
  @media (min-width: 25rem) {
    .Footer-menu .Menu .Menu-item {
      font-size: 0.75rem;
    }
  }
  .Footer-menu .Menu .Menu-item a {
    display: inline-block;
    padding: 0.375rem 0;
  }
  .Footer-menu .Menu .Menu-item ~ .Menu-item {
    margin: 0 0 0 0.125rem;
  }
  .Footer-menu .Menu .Menu-item ~ .Menu-item:before {
    display: inline-block;
    margin: 0 0.4375rem 0 0;
    content: "|";
    color: #999;
  }
  .Footer-copyright {
    color: #666;
    font-size: 0.625rem;
    line-height: 1;
    white-space: pre;
  }
  .Footer-copyright {
    display: none;
  }
  @media (min-width: 25rem) {
    .Footer-copyright {
      font-size: 0.75rem;
      line-height: 1.5;
    }
    .Footer-copyright {
      display: block;
    }
  }
  .Icon {
    position: relative;
    display: inline-block;
    min-width: 1em;
    min-height: 1em;
  }
  .Icon:after,
  .Icon:before {
    position: absolute;
    z-index: 1;
    display: block;
    content: "";
    -webkit-transition: 0.35s;
    transition: 0.35s;
    background-repeat: no-repeat;
    background-position: center;
    background-size: 1em 1em;
    width: 1em;
    height: 1em;
  }
  .Icon--youtube:before {
    background-image: url(./assets/icons/icon-youtube.svg);
  }
  .Icon--youtube:after {
    background-image: url(./assets/icons/icon-youtube-white.svg);
    z-index: 2;
    opacity: 0.35;
  }
  .Icon--youtube:before {
    opacity: 0;
  }
  .no-touchevents .Icon--youtube:before {
    opacity: 1;
  }
  .no-touchevents .Icon--youtube:after {
    z-index: 2;
    opacity: 0;
  }
  .no-touchevents .Icon--youtube:hover:after {
    opacity: 1;
    z-index: 2;
  }
  .no-touchevents .Icon--youtube:hover:before {
    opacity: 0;
  }
  .Icon--linkedin:before {
    background-image: url(./assets/icons/icon-linkedin.svg);
  }
  .Icon--linkedin:after {
    background-image: url(./assets/icons/icon-linkedin-white.svg);
    z-index: 2;
    opacity: 0.35;
  }
  .Icon--linkedin:before {
    opacity: 0;
  }
  .no-touchevents .Icon--linkedin:before {
    opacity: 1;
  }
  .no-touchevents .Icon--linkedin:after {
    z-index: 2;
    opacity: 0;
  }
  .no-touchevents .Icon--linkedin:hover:after {
    opacity: 1;
    z-index: 2;
  }
  .no-touchevents .Icon--linkedin:hover:before {
    opacity: 0;
  }
  .Icon--facebook:before {
    background-image: url(./assets/icons/icon-facebook.svg);
  }
  .Icon--facebook:after {
    background-image: url(./assets/icons/icon-facebook-white.svg);
    z-index: 2;
    opacity: 0.35;
  }
  .Icon--facebook:before {
    opacity: 0;
  }
  .no-touchevents .Icon--facebook:before {
    opacity: 1;
  }
  .no-touchevents .Icon--facebook:after {
    z-index: 2;
    opacity: 0;
  }
  .no-touchevents .Icon--facebook:hover:after {
    opacity: 1;
    z-index: 2;
  }
  .no-touchevents .Icon--facebook:hover:before {
    opacity: 0;
  }

  a {
    text-decoration: none;
  }
  h3 {
    color: #404040;
  }
  a,
  p {
    margin: 0;
  }
  p {
    padding-bottom: 18px;
    font-size: 1.125rem;
    line-height: 1.6;
  }
  p:last-child {
    padding-bottom: 0;
  }
  a {
    outline: 0;
  }
  :-moz-placeholder,
  :-ms-input-placeholder,
  ::-moz-placeholder,
  ::-webkit-input-placeholder {
    color: #000;
  }
}
/*! CSS Used from: http://www.achieve3000.com/wp-content/themes/achieve-3000/app/assets/dist/css/qa-style.css ; media=all */
@media all {
  .Footer-copyright {
    display: block;
  }
  .Footer-information .Footer-information-right {
    position: relative;
    height: 42px;
  }
  .Footer-information .Footer-information-right p {
    position: absolute;
    bottom: 0;
    right: 0;
    font-size: 0.75rem;
    line-height: 1.5;
  }
  .Footer-information .Footer-information-right p a {
    color: #666 !important;
    font-weight: 400 !important;
  }
  .Footer-information .Footer-information-right p a:hover {
    color: #254e70 !important;
  }
  @media (max-width: 767px) {
    .Footer-information .Footer-information-right p {
      position: relative;
      text-align: center;
      margin-top: 10px;
    }
  }
}
</style>
