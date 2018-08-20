<template>
  <div>
    <div v-for="item in article" :key="item.id" class="article">
      <div class="article__main " :class="{ 'article--enable' : item.isActive }" >
        <section class="section">
          <div class="container">
            <h1 class="title">{{ item.title }}</h1>
            <h2 class="subtitle">
              {{ item.excerpt }}
            </h2>
          </div>
        </section>
      </div>
      <div class="article__end">
        <button class="button is-info" @click="enableToggle(item.id)" v-if="item.isActive">
          disable
        </button>
        <button class="button is-primary" @click="enableToggle(item.id)" v-else>
          enable
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    computed: {
      article() {
        return this.$store.getters.articles;
      }
    },
    methods:{
      enableToggle(id) {
        let article =  this.$store.getters.getArticleById(id)
        article.isActive = !article.isActive
        const data = {
          title: article.title,
          link:  article.link,
          excerpt: article.excerpt,
          isActive: article.isActive
        }
        const url = 'https://scrape-b2b08.firebaseio.com/data/' + article.pk + '/' + article.date + '/' + article.index + '.json';
        this.$axios.$put(url, data)

        .then(res=>{
          this.$store.dispatch('editArticle', article);
        })
        .catch(res=>{
          console.log(res);
        })

      }
    },
}
</script>
<style scoped>
  .article {
    font-size:0.7rem;
    border:1px solid;
    border-radius: 5px;
    margin:10px;
    align-items: center;
    position: relative;
  }

  .article__end {
    position: absolute;
    top:0;
    right:0;
  }

  .article--enable {
    background: #7fffff;
  }
</style>
