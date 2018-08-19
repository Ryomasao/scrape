<template>
  <div>
    <section class="hero">
      <figure class="image">
        <img src="~/assets/images/hero.jpg">
      </figure>
    </section>
    <div class="wrap">
      <div class="main">
        <section class="section">
          <div class="container">
            <h1 class="title">Section</h1>
            <h2 class="subtitle">
              A simple container to divide your page into <strong>sections</strong>, like the one you're currently reading
            </h2>
          </div>
        </section>
        <section class="section">
          <div class="container">
            <h1 class="title">Section</h1>
            <h2 class="subtitle">
              A simple container to divide your page into <strong>sections</strong>, like the one you're currently reading
            </h2>
          </div>
        </section>
        <section class="section">
          <div class="container">
            <h1 class="title">Section</h1>
            <h2 class="subtitle">
              A simple container to divide your page into <strong>sections</strong>, like the one you're currently reading
            </h2>
          </div>
        </section>
      </div>
      <div class="sidebar">
        <div class="section">
          <List />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import List from '@/components/List'

export default {
  components: {
    List
  },
}
</script>

<style>
  .wrap {
    display: flex;
  }

  .main {
    flex:1;
  }

  .sidebar {
    width: 300px;
  }
</style>
