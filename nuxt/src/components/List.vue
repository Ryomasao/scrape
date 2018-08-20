<template>
    <div class="articles">
        <p>記事の一覧イメージ</p>
        <div v-for="item in article" :key="item.id" class="article">
          <nuxt-link :to="articleLink(item.id)">
            <div class="aricle__title">
              {{item.title}}
            </div>
          </nuxt-link>
        </div>
    </div>
</template>
<script>
export default {
    computed: {
      article() {
        return this.$store.getters.activeArticle;
      }
    },
    methods:{
      articleLink(id) {
        return {path: '/article/' + id}
      }
    },
}
</script>
<style>
  .articles {
    border: 1px solid;
    border-radius: 3px;
    padding:5px;
  }

  .article {
    font-size:0.8rem;
    margin:3px;
  }
</style>
