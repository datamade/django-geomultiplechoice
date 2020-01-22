DATA_DIR = example/data

.PHONY: all
all: $(DATA_DIR)/final/cb_2018_17_bg_500k.shp

clean:
	rm -Rf $(DATA_DIR)/raw/* $(DATA_DIR)/intermediate/* $(DATA_DIR)/final/* && \
			touch $(DATA_DIR)/raw/.gitkeep $(DATA_DIR)/intermediate/.gitkeep \
			$(DATA_DIR)/final/.gitkeep

$(DATA_DIR)/raw/cb_2018_%_bg_500k.zip:
	wget -O $@ https://www2.census.gov/geo/tiger/GENZ2018/shp/$(notdir $@)

$(DATA_DIR)/intermediate/cb_2018_%_bg_500k.shp: $(DATA_DIR)/raw/cb_2018_%_bg_500k.zip
	unzip "$<" -d $(dir $@)

$(DATA_DIR)/final/cb_2018_%_bg_500k.shp: $(DATA_DIR)/intermediate/cb_2018_%_bg_500k.shp
	COUNTIES=$$($(DATA_DIR)/scripts/get_counties_for_state.py $(notdir $*)) && \
	    ogr2ogr -dialect SQLite -sql "SELECT * FROM $(notdir $(basename $@)) WHERE COUNTYFP in $$COUNTIES" $@ $<
