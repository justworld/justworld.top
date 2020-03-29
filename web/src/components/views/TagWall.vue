<template>
  <div class="tag-wall">
    <panel :title="'标签墙'">
      <div slot="content" class="content">
        <iv-tag v-for="(tag, index) in tagList" type="dot" :color="index | mapTagColor" :key="index" style="margin: 0 5px 5px 0;" class="dot-tag"><a style="color:#777" :href="'/articles/?tag='+tag.id">{{ tag.name +' ['+ tag.link_num + ']'}}</a>
        </iv-tag>
      </div>
    </panel>
  </div>
</template>

<script type="text/ecmascript-6">
import Panel from '@/components/utils/Panel'
import {mixin} from '@/utils/index'
export default {
  data () {
    return {
      tagList: []
    }
  },
  components: {
    'panel': Panel
  },
  mixins: [mixin],
  created () {
    this.listTag()
  },
  methods: {
    listTag () {
      this.$http({
        url: this.$http.adornUrl('tag/'),
        method: 'get',
        params: this.$http.adornParams()
      }).then(res => {
        if (res && res.data) {
          this.tagList = res.data.data
        }
      })
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../../common/stylus/index.styl";

  .tag-wall
    .content
      padding 5px 20px

</style>
