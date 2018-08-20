<template>
  <div>
    <a :href="article.link">
        <section class="section">
          <div class="container">
            <h1 class="title">{{ article.title }}</h1>
            <h2 class="subtitle">
              {{ article.excerpt }}
            </h2>
          </div>
        </section>
    </a>
  </div>
</template>

<script>
export default {
  computed: {
    article() {
      const id = this.$route.params.id;
      return  this.$store.getters.getArticleById(id);
    }
  },
}
</script>

