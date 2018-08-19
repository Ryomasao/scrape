<template>
  <div>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <a class="navbar-item" href="https://bulma.io">
                <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28">
            </a>
            <div class="navbar-burger burger" v-bind:class="{ 'is-active': isActive}" @click="isActive = !isActive">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <transition name="fade">
          <div class="navbar-menu" v-bind:class="{ 'is-active': isActive}">
              <div class="navbar-start">
                  <nuxt-link to="/" class="navbar-item">
                    Home
                  </nuxt-link>
                  <nuxt-link to="/admin" class="navbar-item">
                    Admin
                  </nuxt-link>
              </div>
          </div>
        </transition>
    </nav>
    <nuxt/>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isActive: false,
    }
  },
  methods: {

  },
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
