import Vuex from 'vuex';

const createStore = () => {
  return new Vuex.Store({
    state: {
      article: [],
    },
    mutations: {
      setArticle(state, article) {
        state.article = article;
      },
      editArticle(state, editedArticle) {
        const index = state.article.findIndex(
          article => article.id === editedArticle.id
        );
        state.article[index] = editedArticle;
      },
    },
    actions: {
      nuxtServerInit(vuexContext, context) {
        const url = 'https://scrape-b2b08.firebaseio.com/data.json';
        return context.app.$axios.$get(url)
        .then(res => {
          const list = [];

          //最新の結果だけ取得する
          let targetData = '00000000000000';
          let pk = '';
          let date = '';

          for(const key in res) {
            if(res[key] > targetData) {
               targetData = res[key];
               pk = key;
               date = Object.keys(targetData)
            }
          }

          let count = 0;
          const article = targetData[date];
          for(const index in article) {
            list.push({
              id: pk + '_' + index + '_' + count,
              pk: pk,
              date: date[0],
              index: count,
              title: article[index].title,
              link: article[index].link,
              excerpt: article[index].excerpt,
              isActive: article[index].isActive,
            })
            count++;
          }

          vuexContext.commit('setArticle', list)
        })
      },
      setArticle(vuexContext, article) {
        vuexContext.commit('setArticle', article)
      },
      editArticle(vuexContext, article) {
        vuexContext.commit('editArticle', article)
      },
    },
    getters: {
      articles(state) {
        return state.article;
      },
      getArticleById: (state) => (id) => {
        return state.article.find(article => article.id === id);
      },
      activeArticle(state) {
        return state.article.filter(
          item => {
            return item.isActive == true
          }
        )
      },
    },
  });
};

export default createStore;