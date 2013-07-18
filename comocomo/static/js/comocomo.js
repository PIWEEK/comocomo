// Generated by CoffeeScript 1.6.3
(function() {
  var ChosenFoodKindView, FoodKind, FoodKindCollection, FoodType, FoodTypeCollection, FoodTypeSelectView, SlotView, slotView, _ref, _ref1, _ref2, _ref3, _ref4, _ref5, _ref6,
    __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  FoodKind = (function(_super) {
    __extends(FoodKind, _super);

    function FoodKind() {
      _ref = FoodKind.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    return FoodKind;

  })(Backbone.Model);

  FoodKindCollection = (function(_super) {
    __extends(FoodKindCollection, _super);

    function FoodKindCollection() {
      _ref1 = FoodKindCollection.__super__.constructor.apply(this, arguments);
      return _ref1;
    }

    FoodKindCollection.prototype.model = FoodKind;

    return FoodKindCollection;

  })(Backbone.Collection);

  FoodType = (function(_super) {
    __extends(FoodType, _super);

    function FoodType() {
      _ref2 = FoodType.__super__.constructor.apply(this, arguments);
      return _ref2;
    }

    return FoodType;

  })(Backbone.Model);

  FoodTypeCollection = (function(_super) {
    __extends(FoodTypeCollection, _super);

    function FoodTypeCollection() {
      _ref3 = FoodTypeCollection.__super__.constructor.apply(this, arguments);
      return _ref3;
    }

    FoodTypeCollection.prototype.model = FoodType;

    return FoodTypeCollection;

  })(Backbone.Collection);

  SlotView = (function(_super) {
    __extends(SlotView, _super);

    function SlotView() {
      _ref4 = SlotView.__super__.constructor.apply(this, arguments);
      return _ref4;
    }

    SlotView.prototype.el = 'body.comocomo-slot-page';

    SlotView.prototype.events = {
      'click .comocomo-kind-button': 'onClickKindButton'
    };

    SlotView.prototype.initialize = function() {
      var _this = this;
      this.foodKinds = new FoodKindCollection();
      this.foodTypes = new FoodTypeCollection();
      $.ajax({
        url: '/food_kinds/',
        success: function(data, textStatus, jqXHR) {
          return _this.foodKinds.reset(data);
        }
      });
      return $.ajax({
        url: '/food_types/',
        success: function(data, textStatus, jqXHR) {
          return _this.foodTypes.reset(data);
        }
      });
    };

    SlotView.prototype.onClickKindButton = function(event) {
      var chosen, kind, target, type_select;
      target = $(event.currentTarget);
      kind = this.foodKinds.get(target.data('comocomo-kind-id'));
      chosen = new ChosenFoodKindView({
        'kind': kind
      });
      $('#comocomo-chosen-food-kinds').append(chosen.render().$el.html());
      type_select = new FoodTypeSelectView({
        'kind': kind,
        'foodTypes': this.foodTypes
      });
      $('#comocomo-food-type-selects').append(type_select.render().$el.html());
      $('#comocomo-food-type-selects div[data-role="fieldcontain"]').trigger('create');
      return $('#comocomo-food-type-selects div[data-role="fieldcontain"]').fieldcontain('refresh');
    };

    return SlotView;

  })(Jackbone.View);

  ChosenFoodKindView = (function(_super) {
    __extends(ChosenFoodKindView, _super);

    function ChosenFoodKindView() {
      _ref5 = ChosenFoodKindView.__super__.constructor.apply(this, arguments);
      return _ref5;
    }

    ChosenFoodKindView.prototype.render = function() {
      var kind;
      kind = this.options['kind'];
      this.$el.html("<img src=\"" + (kind.get('icon_path')) + "\"/>");
      return this;
    };

    return ChosenFoodKindView;

  })(Jackbone.View);

  FoodTypeSelectView = (function(_super) {
    __extends(FoodTypeSelectView, _super);

    function FoodTypeSelectView() {
      _ref6 = FoodTypeSelectView.__super__.constructor.apply(this, arguments);
      return _ref6;
    }

    FoodTypeSelectView.prototype.render = function() {
      var is_checked, kind, select_block, type, types, types_block, _i, _len,
        _this = this;
      kind = this.options['kind'];
      types = this.options['foodTypes'].filter(function(item) {
        return item.get('kind_id') === kind.get('id');
      });
      types_block = "";
      for (_i = 0, _len = types.length; _i < _len; _i++) {
        type = types[_i];
        is_checked = (type.get('id') === 93 ? 'checked="checked"' : '');
        types_block += "<input type=\"radio\" data-theme=\"c\" name=\"select-type-" + (kind.get('id')) + "\"\n       id=\"select-type-" + (kind.get('id')) + "-" + (type.get('id')) + "\"\n       value=\"" + (type.get('id')) + "\"" + is_checked + " />\n<label for=\"select-type-" + (kind.get('id')) + "-" + (type.get('id')) + "\">" + (type.get('name')) + "</label>";
      }
      select_block = "<div data-role=\"fieldcontain\">\n    <fieldset data-role=\"controlgroup\">\n        <legend><img src=\"" + (kind.get('icon_path')) + "\"/> " + (kind.get('name')) + "</legend>\n        " + types_block + "\n    </fieldset>\n</div>";
      this.$el.html(select_block);
      return this;
    };

    return FoodTypeSelectView;

  })(Jackbone.View);

  slotView = new SlotView();

}).call(this);
