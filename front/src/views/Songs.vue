<template>
  <div class="page">
    <div class="page-content padding-30 container-fluid">
      <div class="row">
        <div class="col-xl-2 col-md-3 info-panel">
          <div class="card card-shadow">
            <h1 class="text-success">Songs Page</h1>
          </div>
        </div>

        <div class="col-md-12">
          <el-button
            @click="dialogVisible = true; type = 'add'; model = {}"
            type="success"
            icon="el-icon-check"
            circle
          ></el-button>
          <br>
          <br>
          <el-input placeholder="search ..." v-model="search"></el-input>
          <br>
          <br>
          <template>
            <el-table 
                :data="searchTbl"
                empty-text="No Data">
              <el-table-column prop="title" label="Title"></el-table-column>
              <el-table-column prop="artist" label="Artist"></el-table-column>
              <el-table-column label="Operations">
                <template slot-scope="scope">
                  <el-button type="warning" @click="handleEdit(scope.$index, scope.row)" circle>
                    <i class="el-icon-edit"></i>
                  </el-button>
                  <el-button type="danger" @click="handleDelete(scope.$index, scope.row)" circle>
                    <i class="el-icon-delete"></i>
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </template>
        </div>
      </div>
    </div>

    <el-dialog title="Song" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <h3>Title</h3>
      <el-input placeholder="Please input" v-model="model.title"></el-input>
      <br>
      <h3>Artist</h3>
      <el-input placeholder="Please input" v-model="model.artist"></el-input>
      <span slot="footer" class="dialog-footer">
        <hr>
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="success" @click="confirm">Confirm</el-button>
      </span>
    </el-dialog>

    <vue-element-loading :active="isActive" :is-full-screen="true"/>
  </div>
</template>
<script>
import axios from "axios";
import VueElementLoading from "vue-element-loading";

const apiURI = "http://127.0.0.1:8000/api/v1/";
//axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1/';

export default {
  name: "songs",
  mounted() {
    this.getAllSongs();
  },
  data() {
    return {
      songs: [],
      isActive: true,
      dialogVisible: false,
      model: {},
      type: "add",
      search: ''
    };
  },
  methods: {
    confirm() {
      if (this.type === "add") {
        this.add();
      } else {
        this.update();
      }
    },
    update() {
      let self = this;
      axios
        .put(apiURI + "song/" + self.model.id, {
          title: self.model.title,
          artist: self.model.artist
        })
        .then(function(response) {
          self.isActive = false;
          self.dialogVisible = false;
          self.getAllSongs();
        })
        .catch(function(error) {
          self.isActive = false;
          return error;
        });
    },
    add() {
      let self = this;
      axios
        .post(apiURI + "songs/", self.model)
        .then(function(response) {
          self.isActive = false;
          self.dialogVisible = false;
          self.getAllSongs();
        })
        .catch(function(error) {
          self.isActive = false;
          return error;
        });
    },
    handleEdit(index, row) {
      this.type = "update";
      this.isActive = true;
      let self = this;
      axios
        .get(apiURI + "song/" + row.id)
        .then(function(response) {
          var value = response.data;
          self.model = value;
          self.isActive = false;
          self.dialogVisible = true;
        })
        .catch(function(error) {
          self.isActive = false;
          return error;
        });
    },
    handleDelete(index, row) {
      this.isActive = true;
      let self = this;
      axios
        .delete(apiURI + "song/" + row.id)
        .then(function(response) {
          var values = response.data;
          self.getAllSongs();
        })
        .catch(function(error) {
          self.isActive = false;
          return error;
        });
    },
    getAllSongs() {
      this.isActive = true;
      let self = this;
      axios
        .get(apiURI + "songs/")
        .then(function(response) {
          var values = response.data;
          self.songs = values;
          self.isActive = false;
        })
        .catch(function(error) {
          self.isActive = false;
          return error;
        });
    }
  },
  computed: {
    searchTbl: function() {
      return this.songs.filter(
        content =>
          content.title.toLowerCase().indexOf(this.search) !== -1 ||
          content.artist.toLowerCase().indexOf(this.search) !== -1
      );
    }
  }
};
</script>
