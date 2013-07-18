class FoodKind extends Backbone.Model

class FoodKindCollection extends Backbone.Collection
    model: FoodKind


class FoodType extends Backbone.Model

class FoodTypeCollection extends Backbone.Collection
    model: FoodType


class SlotView extends Jackbone.View

    el: 'body.comocomo-slot-page'

    events:
        'click .comocomo-kind-button': 'onClickKindButton'

    initialize: ->
        @foodKinds = new FoodKindCollection()
        @foodTypes = new FoodTypeCollection()

        $.ajax(
            url: '/food_kinds/'    # TODO: parametrizar este url de algún modo
            success: (data, textStatus, jqXHR) =>
                @foodKinds.reset(data)
        )

        $.ajax(
            url: '/food_types/'    # TODO: parametrizar este url de algún modo
            success: (data, textStatus, jqXHR) =>
                @foodTypes.reset(data)
        )

    onClickKindButton: (event) ->
        target = $(event.currentTarget)
        kind = @foodKinds.get(target.data('comocomo-kind-id'))

        chosen = new ChosenFoodKindView({'kind': kind})
        $('#comocomo-chosen-food-kinds').append(chosen.render().$el.html())

        type_select = new FoodTypeSelectView({'kind': kind, 'foodTypes': @foodTypes})
        $('#comocomo-food-type-selects').append(type_select.render().$el.html())
        $('#comocomo-food-type-selects div[data-role="fieldcontain"]').trigger('create')
        $('#comocomo-food-type-selects div[data-role="fieldcontain"]').fieldcontain('refresh')
        #$('#comocomo-food-type-selects').collapsibleset('refresh')
        ##type_select.$('ul').listview('refresh')
        ## See http://stackoverflow.com/questions/5925810/dynamically-adding-li-to-ul-in-jquery-mobile
        #$('#comocomo-food-type-selects').trigger('create')
        #$('#comocomo-food-type-selects ul').listview('refresh')


class ChosenFoodKindView extends Jackbone.View

    render: ->
        kind = @options['kind']
        @$el.html("<img src=\"#{ kind.get('icon_path') }\"/>")
        return @


class FoodTypeSelectView extends Jackbone.View

    render: ->
        kind = @options['kind']
        types = @options['foodTypes'].filter((item) => (item.get('kind_id') == kind.get('id')))

        types_block = ""
        for type in types
            is_checked = (if type.get('id') == 93 then 'checked="checked"' else '')
            types_block += """
                           <input type="radio" data-theme="c" name="select-type-#{ kind.get('id') }"
                                  id="select-type-#{ kind.get('id') }-#{ type.get('id') }"
                                  value="#{ type.get('id') }"#{ is_checked } />
                           <label for="select-type-#{ kind.get('id') }-#{ type.get('id') }">#{ type.get('name') }</label>
                           """

        select_block = """
                       <div data-role="fieldcontain">
                           <fieldset data-role="controlgroup">
                               <legend><img src="#{ kind.get('icon_path') }"/> #{ kind.get('name') }</legend>
                               #{ types_block }
                           </fieldset>
                       </div>
                       """
            # TODO: investigate a bit more in this presentation instead of <legend>, possibly nicer
            # <ul data-role="listview" data-split-icon="delete" data-split-theme="a" data-inset="true">
            #     <li><a href="#"><img src="{{ kind.icon_path }}"/> {{ kind.name }}</a><a href="#">delete</a></li>
            # </ul>

        #types_block = ""
        #for type in types
        #    types_block += """
        #                   <li data-icon="False">#{ type.get('name') }</li>
        #                   """

        #select_block = """
        #               <div data-role="collapsible" data-content-theme="c" data-collapsed="false">
        #                   <h2><img src="#{ kind.get('icon_path') }"/> #{ kind.get('name') }</h2>
        #                   <ul data-role="listview">
        #                       #{ types_block }
        #                   </ul>
        #               </div>
        #               """

        @$el.html(select_block)
        return @


slotView = new SlotView()

