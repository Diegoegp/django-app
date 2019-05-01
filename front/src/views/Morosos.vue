<template>
  <div class="page">
    <div class="page-content padding-30 container-fluid">
      <div class="row">
        <div class="col-xl-2 col-md-3 info-panel">
          <div class="card card-shadow">
            <h1 class="text-success">Section - Morosos</h1>
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
            <el-table :data="searchTbl" empty-text="No Data">
              <el-table-column prop="name" label="name"></el-table-column>
              <el-table-column prop="last_name" label="last_name"></el-table-column>
              <el-table-column prop="cellphone" label="cellphone"></el-table-column>
              <el-table-column prop="no_apto" label="no_apto"></el-table-column>
              <el-table-column prop="balance" label="balance"></el-table-column>
              <el-table-column prop="status" label="status"></el-table-column>
              <el-table-column prop="date" label="date"></el-table-column>

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

    <el-dialog title="Moroso" :visible.sync="dialogVisible" width="30%">
      <div class="row">
        <div class="col-md-6">
          <h3>Name</h3>
          <el-input placeholder="Please input" v-model="model.name"></el-input>
          <br>
          <h3>Last Name</h3>
          <el-input placeholder="Please input" v-model="model.last_name"></el-input>
          <br>
          <h3>cellphone</h3>
          <el-input placeholder="Please input" v-model="model.cellphone"></el-input>
          <br>
          <h3>no_apto</h3>
          <el-input placeholder="Please input" v-model="model.no_apto"></el-input>
          <br>
          <h3>balance</h3>
          <el-input placeholder="Please input" v-model="model.balance"></el-input>
        </div>
        <div class="col-md-6">
          <h3>date</h3>
          <el-date-picker
            format="yyyy-MM-dd HH:mm"
            v-model="model.date"
            type="datetime"
            placeholder="Select date and time"
          ></el-date-picker>
          <br>
          <h3>comment</h3>
          <el-input type="textarea" :rows="6" placeholder="Please input" v-model="model.comment"></el-input>
          <br>
          <h3>month</h3>    
            <el-select v-model="model.month" placeholder="--">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"></el-option>
            </el-select>                
          <br>
          <h3>status</h3>
           <el-select v-model="model.status" placeholder="--">
              <el-option
                v-for="item in statuslist"
                :key="item.value"
                :label="item.label"
                :value="item.value"></el-option>
            </el-select> 
        </div>
      </div>

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
  name: "morosos",
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
      search: "",
      statuslist: [
        {
          value: 'MOROSO',
          label: 'Moroso'
        },
        {
          value: 'VIGENTE',
          label: 'Vigente'
        }
      ],
       options: [{
          value: '1',
          label: 'Enero'
        }, {
          value: '2',
          label: 'Febrero'
        }, {
          value: '3',
          label: 'Marzo'
        }, {
          value: '4',
          label: 'Abril'
        }, {
          value: '5',
          label: 'Mayo'
        },{
          value: '6',
          label: 'Junio'
        },{
          value: '7',
          label: 'Julio'
        }, {
          value: '8',
          label: 'Agosto'
        }, {
          value: '9',
          label: 'Septiembre'
        }, {
          value: '10',
          label: 'Octubre'
        }, {
          value: '11',
          label: 'Noviembre'
        },{
          value: '12',
          label: 'Diciembre'
        }]
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
        .put(apiURI + "moroso/" + self.model.id, self.model)
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
        .post(apiURI + "morosos/", self.model)
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
        .get(apiURI + "moroso/" + row.id)
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
        .delete(apiURI + "moroso/" + row.id)
        .then(function(response) {
          console.log(response);
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
        .get(apiURI + "morosos/")
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
          content.name.toLowerCase().indexOf(this.search) !== -1 ||
          content.last_name.toLowerCase().indexOf(this.search) !== -1
      );
    }
  }
};
</script>
