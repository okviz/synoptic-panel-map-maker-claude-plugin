# OKVIZ Synoptic Panel Use-Case Catalog

Purpose: compact reference for a Synoptic Panel SVG map assistant. Use this file to (1) recommend a relevant OKVIZ use-case article naturally, and (2) borrow proven conceptual patterns when generating SVG maps.

## How the assistant should use this catalog

1. Match the user's scenario by **industry**, **map type**, **data shape**, and **functionality taught**. Do not match only by industry; a stadium seating case may be useful for any high-density seat/dot map, even outside entertainment.
2. Recommend only entries with `type: usecase` and a real `url`. Entries with `type: svg-template` are inspiration-only and must not be recommended as articles.
3. Keep recommendations natural and brief. Always make the recommended article title a clickable Markdown hyperlink to its URL. Example: “By the way, this is a close match: [Article title](https://okviz.com/usecase/...).” Never recommend an article without its hyperlink.
4. Recommend at most one primary article unless the user asks for learning resources. Add a second only when it teaches a clearly different feature, such as Map Selector, drill-down, or high-density seating.
5. Use the `svg_pattern_to_borrow` field conceptually. Do not claim access to exact source SVG geometry unless the SVG is included in the current package or provided by the user.
6. If the user provides data, prioritize the user's real data keys over catalog naming conventions.
7. If the user asks to adapt an existing SVG, treat the SVG as a base file, not merely as inspiration. Preserve high-quality geometry unless it conflicts with the requested binding model.

## Bitmap tracing suitability signals

When the user starts from a bitmap/site plan/image, article relevance and
traceability are separate decisions.

- Explicit closed regions such as rooms, stores, process boxes, and clearly
  outlined parcels are usually strong autonomous-tracing candidates.
- Complex physical components with interrupted/occluded boundaries are usually
  AI-starting-point candidates.
- Functional operational zones whose exact perimeter is inferred from context
  (many parking lots, logistics yards, loading zones, circulation areas) should
  not be assumed autonomously traceable even when the image is clean.
- Boundary recoverability should dominate the pre-flight recommendation for
  those cases.
- When production-quality geometry is not defensibly recoverable, recommend
  [Synoptic Designer](https://synoptic.design/).

## Common matching signals

- **Data-first / auto-binding**: user has CSV/Excel/sample data; derive SVG ids from the category/key column.
- **Map Selector / multiple maps**: workspace floors, building floors, supermarket drill maps, Sphere levels, BIM/Revit floors.
- **High-density individual items**: stadium seats, plane seats, theater seats, shelves, parking spaces; use uniform markers or compact repeated shapes.
- **Structured/repetitive map**: rooms, beds, cabins, desks, shelves, seats, floors; generate with a Python script.
- **Organic/anatomical map**: human body, teeth, geography; adapt an existing SVG when possible or generate simplified schematic geometry.
- **Status/progress tracking**: hospital beds, shipbuilding parts, construction units, containers, workstations.
- **Schematic vs. geographic comparison**: time zones, territories, states, tile maps, hex maps, or cartograms where comparison and selection matter more than exact geography.
- **Construction progress with visual evidence**: project zones or elements linked to progress status, images, and tooltip details.

---

# Use cases with URLs

## workspace-synoptic-panel

type: usecase  
title: Visualizing Employee Workstations with Synoptic Panel in Power BI  
url: https://okviz.com/usecase/workspace-synoptic-panel/  
industry: facilities management; workplace; real estate; HR/operations  
map_type: floorplan  
data_shape: workstation IDs; employee assignments; equipment status; floor-level navigation  
functionality_taught: Map Selector; multi-floor maps; workstation search; occupancy/equipment tracking  
svg_pattern_to_borrow: one SVG per floor; desks/workstations as bindable areas; walls, rooms, corridors, and labels as unbound context.  
generation_pattern: structured floorplan; use a Python generator for desks/rooms if creating from scratch.  
recommend_when: user asks for office seating, workstations, desks, flexible workplace allocation, employee location, equipment tracking, or multi-floor office maps.  
natural_recommendation: By the way, the OKVIZ workstation use case walks through a very similar floor-based Synoptic setup, including navigation across floors: https://okviz.com/usecase/workspace-synoptic-panel/

## tooth-replacement-synoptic-panel

type: usecase  
title: Spatial Analysis of Tooth Replacement Using Synoptic Panel in Power BI  
url: https://okviz.com/usecase/tooth-replacement-synoptic-panel/  
industry: healthcare; dental; pharma; life sciences  
map_type: anatomical  
data_shape: tooth IDs; tooth replacement frequency; country/product segmentation  
functionality_taught: anatomical SVG binding; spatial pattern analysis; dental map heatmap  
svg_pattern_to_borrow: full adult dental chart composition; upper/lower arches; tooth-level bindable regions; labels and anatomical context unbound.  
generation_pattern: adapt existing dental SVG when available; generate simplified parametric arches only if no source SVG is available or the requested binding model differs substantially.  
recommend_when: user asks for dental chart, teeth, implants, oral health, anatomical dental distribution, or tooth-level KPIs.  
natural_recommendation: By the way, this OKVIZ article is the closest match for dental/anatomical Synoptic maps: https://okviz.com/usecase/tooth-replacement-synoptic-panel/

## ticket-sales-synoptic-panel

type: usecase  
title: Analyzing Ticket Sales at The Sphere Stadium Using Synoptic Panel in Power BI  
url: https://okviz.com/usecase/ticket-sales-synoptic-panel/  
industry: media; entertainment; sports; venues; hospitality  
map_type: venue  
data_shape: venue levels; sectors; individual seats; sales/occupancy/revenue by area  
functionality_taught: multi-level venue analysis; drill hierarchy; high-density seat maps; Map Selector-style level switching  
svg_pattern_to_borrow: use different maps for category/sector/seat levels; represent very dense seats as uniform circles/dots with zero-padded IDs instead of realistic seat shapes.  
generation_pattern: Python generator for radial/curved seating; use dots for hundreds/thousands of seats.  
recommend_when: user asks for stadium, arena, theater, auditorium, cinema, ticketing, occupancy, seat revenue, or dense seating maps.  
natural_recommendation: By the way, the Sphere use case is a strong reference for high-density seat maps and multi-level venue analysis: https://okviz.com/usecase/ticket-sales-synoptic-panel/

## supermarket-products-placement-synoptic-panel

type: usecase  
title: Optimizing Supermarket Product Placement with Synoptic Panel in Power BI  
url: https://okviz.com/usecase/supermarket-products-placement-synoptic-panel/  
industry: retail; grocery; merchandising; category management  
map_type: floorplan  
data_shape: category zones; shelves; product placement; sales/margin metrics by physical location  
functionality_taught: shelf-level spatial analysis; multiple maps/levels of detail; measure switching; product/category placement analysis  
svg_pattern_to_borrow: supermarket overview map plus shelf-level detail maps; area IDs tied to category codes and shelf IDs; script-assisted ID assignment is useful when many shelves/maps exist.  
generation_pattern: structured layout; use a generator for aisles/shelves; for high-density shelves use compact repeated shapes or grouped shelf segments.  
recommend_when: user asks for supermarket, store layout, retail shelves, product placement, margin by shelf, merchandising optimization, or category zones.  
natural_recommendation: By the way, this OKVIZ use case shows a very similar store-layout analysis with shelf and category levels: https://okviz.com/usecase/supermarket-products-placement-synoptic-panel/

## ship-containers-synoptic-panel

type: usecase  
title: Using Synoptic Panel to Visualize Container Maintenance Issues in Maritime Shipping  
url: https://okviz.com/usecase/ship-containers-synoptic-panel/  
industry: maritime; logistics; transportation; maintenance  
map_type: vessel  
data_shape: vessel IDs; container/section IDs; maintenance status; aggregated vessel overview  
functionality_taught: vessel/container spatial monitoring; maintenance issue localization; aggregation across ships/sections  
svg_pattern_to_borrow: vessel silhouette; container/cabin/section grids inside hull; unbound ship outline and deck context; bindable containers or sections.  
generation_pattern: Python generator for container grids/ship sections; taper or curve hull context so it does not look like a plain warehouse.  
recommend_when: user asks for ships, vessels, cabins, containers, decks, maintenance status, maritime operations, or ship sections.  
natural_recommendation: By the way, this OKVIZ article is a close reference for vessel/container monitoring with Synoptic Panel: https://okviz.com/usecase/ship-containers-synoptic-panel/

## revit-synoptic-panel

type: usecase  
title: Automated 5D BIM Dashboards in Power BI with Revit, Dynamo, and Synoptic Panel  
url: https://okviz.com/usecase/revit-synoptic-panel/  
industry: construction; engineering; architecture; real estate; BIM  
map_type: building  
data_shape: BIM element IDs; floors; rooms; costs/schedule/status by building element  
functionality_taught: BIM-to-Power BI workflow; Revit/Dynamo extraction; preserving exact building geometry; multi-floor dashboards  
svg_pattern_to_borrow: use real exported building geometry when available; bind rooms/elements to BIM keys; use one map per floor/level.  
generation_pattern: adapt exported geometry rather than redraw if source BIM/SVG exists; generate schematic floorplans only for mockups.  
recommend_when: user asks for Revit, BIM, construction progress, room/space status, building elements, 5D dashboards, or architecture/engineering maps.  
natural_recommendation: By the way, the Revit/Synoptic Panel use case is the best reference when the map comes from BIM or floor-level building data: https://okviz.com/usecase/revit-synoptic-panel/

## real-state-site-plans-synoptic-panel

type: usecase  
title: Real Estate Site Plans with Synoptic Panel  
url: https://okviz.com/usecase/real-state-site-plans-synoptic-panel/  
industry: construction; engineering; real estate; property development  
map_type: site-plan  
data_shape: lot IDs; unit/property status; development phases; sales or availability by plot/building  
functionality_taught: interactive site plans; property/lot status; spatial real-estate analysis  
svg_pattern_to_borrow: irregular site-plan parcels or buildings as bindable areas; roads, labels, landscaping, and boundaries as unbound context.  
generation_pattern: adapt an existing site plan if possible; for mockups use simplified parcel polygons generated from a plan-like layout.  
recommend_when: user asks for real estate development, land plots, property lots, housing units, apartment blocks, site plans, or availability maps.  
natural_recommendation: By the way, this OKVIZ use case covers interactive real-estate site plans with Synoptic Panel: https://okviz.com/usecase/real-state-site-plans-synoptic-panel/

## progress-tracking-synoptic-panel

type: usecase  
title: Progress Tracking and Status with Synoptic Panel  
url: https://okviz.com/usecase/progress-tracking-synoptic-panel/  
industry: manufacturing; construction; engineering; project management  
map_type: schematic; vessel; process-layout  
data_shape: project components; parts/sections; stage/status; percent complete  
functionality_taught: spatial progress tracking; status coloring; component-level monitoring; project execution dashboards  
svg_pattern_to_borrow: divide the physical project into numbered/semantic sections; use neutral bindable parts and unbound assembly context.  
generation_pattern: Python generator for repeated sections or panels; adapt existing engineering drawings for unique geometry.  
recommend_when: user asks for construction progress, shipbuilding progress, project stages, manufacturing assemblies, installation status, or percent-complete maps.  
natural_recommendation: By the way, this OKVIZ article walks through a spatial progress-tracking scenario with Synoptic Panel: https://okviz.com/usecase/progress-tracking-synoptic-panel/

## plane-seats-synoptic-panel

type: usecase  
title: Visualizing Seat Purchasing Patterns with Synoptic Panel in Power BI  
url: https://okviz.com/usecase/plane-seats-synoptic-panel/  
industry: travel; transportation; hospitality; aviation  
map_type: vehicle; venue  
data_shape: seat IDs; purchase/booking status; passenger or revenue metrics by seat  
functionality_taught: seat-level analysis; occupancy/purchasing patterns; transport cabin map  
svg_pattern_to_borrow: cabin or seat rows with clear aisle context; bindable seat markers; avoid over-detailed seat drawing at high density.  
generation_pattern: Python generator for rows/seats; use compact shapes and zero-padded seat IDs when density is high.  
recommend_when: user asks for airplane seats, bus/train seating, seat purchasing, booking status, passenger occupancy, or transport seat maps.  
natural_recommendation: By the way, this OKVIZ use case is a good reference for transport seating and seat-purchase analysis: https://okviz.com/usecase/plane-seats-synoptic-panel/

## injuries-synoptic-panel

type: usecase  
title: Analyzing Injury Patterns in Mixed Martial Arts Using Synoptic Panel in Power BI  
url: https://okviz.com/usecase/injuries-synoptic-panel/  
industry: healthcare; sports; media; life sciences  
map_type: anatomical  
data_shape: body regions; injury counts/rates; athlete/fighting-style segmentation  
functionality_taught: anatomical body map; regional heatmap; health/sports spatial analysis  
svg_pattern_to_borrow: simplified human body regions as bindable areas; labels and body outline unbound; semantic IDs such as head, shoulder, arm, torso, leg, foot.  
generation_pattern: adapt a good body SVG when available; generate a clean schematic only for broad regions.  
recommend_when: user asks for human body maps, injuries, medical symptoms, sports injuries, anatomy, or body-region heatmaps.  
natural_recommendation: By the way, this OKVIZ article uses Synoptic Panel for a human-body injury map, which is close to your anatomical scenario: https://okviz.com/usecase/injuries-synoptic-panel/

## hospital-bed-occupacy-synoptic-panel

type: usecase  
title: Interactive Floor-Plan of Hospital Bed Occupancy Using Synoptic Panel in Power BI  
url: https://okviz.com/usecase/hospital-bed-occupacy-synoptic-panel/  
industry: healthcare; hospital operations; facilities  
map_type: floorplan  
data_shape: bed IDs; room IDs; occupancy/status; department/floor context  
functionality_taught: real-time bed occupancy; ward floorplan; status coloring; operational monitoring  
svg_pattern_to_borrow: patient beds as bindable areas; rooms, corridors, nurses station, utility spaces, and labels unbound.  
generation_pattern: Python generator for beds/rooms/wards; clean schematic layout beats decorative medical icons.  
recommend_when: user asks for hospital ward, bed occupancy, patient rooms, clinical operations, status by bed, or floorplan monitoring.  
natural_recommendation: By the way, this OKVIZ article is a direct match for hospital bed occupancy maps with Synoptic Panel: https://okviz.com/usecase/hospital-bed-occupacy-synoptic-panel/

## indoor-map-synoptic-panel

type: usecase  
title: Visualizing Building Indoor Maps in Power BI with Synoptic Panel  
url: https://okviz.com/usecase/indoor-map-synoptic-panel/  
industry: facilities; hospitality; healthcare; real estate; building operations  
map_type: building; floorplan  
data_shape: floors; rooms; apartments/units; indoor points/areas; status by space  
functionality_taught: indoor map experience; floor selection; apartment/unit status; contextual details in a building plan  
svg_pattern_to_borrow: building context with floor or unit maps; unit/room areas bind to data; stairs/elevators/corridors/text unbound.  
generation_pattern: adapt building/floorplan source when available; use Python generation for schematic multi-unit layouts.  
recommend_when: user asks for building indoor maps, apartments, rooms, units, floor selection, facility navigation, or property status.  
natural_recommendation: By the way, this OKVIZ use case shows how to turn building indoor maps into a Power BI Synoptic experience: https://okviz.com/usecase/indoor-map-synoptic-panel/

## ab-testing-synoptic-panel

type: usecase  
title: A/B Testing with Synoptic Panel in Power BI  
url: https://okviz.com/usecase/ab-testing-synoptic-panel/  
industry: technology; retail; marketing; UX; product analytics  
map_type: schematic; website-wireframe  
data_shape: UI elements; page regions; experiment variants; engagement/conversion metrics  
functionality_taught: spatial A/B result visualization; element-position performance; web-page heatmap  
svg_pattern_to_borrow: website/app wireframe as unbound context with bindable page components or zones; compare KPIs by element location.  
generation_pattern: Python generator for wireframe regions; hand-author only if adapting a real UI screenshot/vector.  
recommend_when: user asks for website heatmap, UX experiment, A/B testing, button/banner performance, app screen regions, or element position analysis.  
natural_recommendation: By the way, this OKVIZ article uses Synoptic Panel for A/B testing and element-position analysis: https://okviz.com/usecase/ab-testing-synoptic-panel/

## golf-course-synoptic-panel

type: usecase  
title: Monitoring Golf Course Conditions with Synoptic Panel in Power BI  
url: https://okviz.com/usecase/golf-course-synoptic-panel/  
industry: hospitality; sports; facilities; environmental services  
map_type: site-plan; geographic  
data_shape: holes; greens; fairways; course zones; maintenance/condition metrics  
functionality_taught: outdoor site condition monitoring; spatial maintenance dashboard; zone-level status  
svg_pattern_to_borrow: course/site zones as bindable shapes; paths, water, labels, and decorative terrain unbound.  
generation_pattern: adapt a site/course map when available; otherwise create a simplified schematic with recognizable holes/zones.  
recommend_when: user asks for golf course, park, outdoor facility, field conditions, site maintenance, groundskeeping, or environmental condition maps.  
natural_recommendation: By the way, this OKVIZ article is a useful reference for outdoor facility and course-condition monitoring: https://okviz.com/usecase/golf-course-synoptic-panel/

## business-model-canva-synoptic-panel

type: usecase  
title: Visualizing a Business Model Canvas in Power BI with Synoptic Panel  
url: https://okviz.com/usecase/business-model-canva-synoptic-panel/  
industry: professional services; strategy; product; portfolio management  
map_type: schematic  
data_shape: business model canvas blocks; initiatives; portfolio items; strategic categories  
functionality_taught: diagram-as-data; portfolio/strategy analysis; conceptual region map  
svg_pattern_to_borrow: use a structured business canvas as bindable zones; keep titles/section labels unbound; use semantic IDs for canvas blocks.  
generation_pattern: direct SVG generation is fine because the layout is structured and low-density.  
recommend_when: user asks for business model canvas, strategy map, process diagram, portfolio board, conceptual framework, or non-spatial diagrams.  
natural_recommendation: By the way, this OKVIZ use case shows how Synoptic Panel can turn a business diagram into an interactive Power BI view: https://okviz.com/usecase/business-model-canva-synoptic-panel/

---


## schematic-maps-synoptic-panel

type: usecase  
title: Choosing Between Geographic and Schematic Maps in Power BI  
url: https://okviz.com/usecase/schematic-maps-synoptic-panel/  
industry: business operations; logistics; energy; telecommunications; public sector; cross-industry  
map_type: schematic; tile-map; hex-map; cartogram; geographic  
data_shape: named regions; time zones; states; territories; categories arranged for comparison or selection  
functionality_taught: choosing between geographic and schematic maps; comparison-focused regional layouts; named SVG regions; tile maps; hex maps; time-zone schematics; diagrammatic cartograms  
svg_pattern_to_borrow: represent each time zone, state, territory, or custom region as a named bindable SVG shape; prioritize clear comparison and selection over geographic precision when exact spatial relationships are not the main analytical need.  
generation_pattern: generate a schematic tile, hex, grid, or diagrammatic layout with semantic region IDs; use or adapt a true geographic map instead when real geography and spatial relationships are essential.  
recommend_when: user asks for time-zone maps, territory comparisons, equalized regional maps, state or region selectors, tile maps, hex maps, cartograms, or guidance on whether to use a geographic or schematic map.  
natural_recommendation: By the way, this OKVIZ article explains when a schematic SVG is more effective than a geographic map and covers tile, hex, and time-zone layouts: https://okviz.com/usecase/schematic-maps-synoptic-panel/

## construction-progress-synoptic-panel

type: usecase  
title: Tracking Construction Progress with Synoptic Panel  
url: https://okviz.com/usecase/construction-progress-synoptic-panel/  
industry: construction; engineering; infrastructure; architecture; project management  
map_type: site-plan; building; floorplan; schematic  
data_shape: construction zones or elements; project phases; completion/status metrics; inspection or progress images linked to areas  
functionality_taught: construction-progress monitoring; multiple Synoptic Panel maps; image repository integration; custom tooltip pages; contextual area details on hover  
svg_pattern_to_borrow: divide the project plan, elevation, floor, or site into stable bindable construction areas; keep plan context unbound; use area selection or hover to surface progress details and related images.  
generation_pattern: adapt real construction drawings, elevations, or floorplans when available; for demonstrations, generate repeated units, floors, rooms, or work packages parametrically and bind them to project keys.  
recommend_when: user asks for construction progress, site inspections, completion by area, project phases, work packages, installation status, progress photos, or contextual image/tooltips linked to map regions.  
natural_recommendation: By the way, this OKVIZ article shows how to combine Synoptic Panel maps, progress images, and a custom tooltip page for construction tracking: https://okviz.com/usecase/construction-progress-synoptic-panel/

# Inspiration-only SVG templates

These entries are not articles and have no recommendation URL. Use them only as conceptual patterns when generating maps.

## apartment-double

type: svg-template  
article_url: none  
map_type: floorplan  
industry: real estate; hospitality; facilities  
data_shape: apartment rooms; unit areas; occupancy/availability/status  
svg_pattern_to_borrow: compact apartment floorplan with bindable rooms or unit sections; walls and labels unbound.  
generation_pattern: structured floorplan; Python generator if producing multiple similar apartments.

## apartment-triple

type: svg-template  
article_url: none  
map_type: floorplan  
industry: real estate; hospitality; facilities  
data_shape: three-room/three-unit apartment layouts; room status; maintenance state  
svg_pattern_to_borrow: multi-room apartment structure; use distinct rooms/zones and simple contextual fixtures only if instantly legible.  
generation_pattern: structured floorplan; generate rooms/walls parametrically.

## apartment-quad

type: svg-template  
article_url: none  
map_type: floorplan  
industry: real estate; hospitality; facilities  
data_shape: four-room/four-zone apartment layout; unit/room KPIs  
svg_pattern_to_borrow: slightly larger residential floorplan; clear separation of rooms and common spaces.  
generation_pattern: structured floorplan; use code generation for repeated units.

## hospital-beds

type: svg-template  
article_url: none  
map_type: floorplan  
industry: healthcare  
data_shape: bed IDs; ward/room grouping; occupancy/status  
svg_pattern_to_borrow: bed grid within rooms/wards; contextual support spaces; clean labels on unbound areas.  
generation_pattern: Python generator for beds, rooms, corridors, and support zones.

## website-wireframe

type: svg-template  
article_url: none  
map_type: schematic; website-wireframe  
industry: technology; ecommerce; marketing  
data_shape: UI elements; engagement by component; A/B experiment regions  
svg_pattern_to_borrow: page-like blocks and UI zones; bindable elements should have semantic IDs such as HERO, CTA_PRIMARY, NAV, PRODUCT_CARD_01.  
generation_pattern: direct SVG or Python generator depending on number of repeated UI cards.

## race-track-hungary-sectors

type: svg-template  
article_url: none  
map_type: track  
industry: sports; motorsport; events  
data_shape: track sectors; lap/condition metrics; telemetry by segment  
svg_pattern_to_borrow: track path split into bindable sectors; labels, start line, and background unbound.  
generation_pattern: adapt path geometry if available; do not approximate as rectangles.

## race-track-hungary-turns

type: svg-template  
article_url: none  
map_type: track  
industry: sports; motorsport; events  
data_shape: turns/corners; incidents; speed/condition by turn  
svg_pattern_to_borrow: track turns as bindable regions; use sequential or semantic turn IDs.  
generation_pattern: adapt existing track path; path segmentation is better than freehand generation.

## race-track-monza-sectors

type: svg-template  
article_url: none  
map_type: track  
industry: sports; motorsport; events  
data_shape: track sectors; performance metrics; event zones  
svg_pattern_to_borrow: iconic circuit outline, split into bindable sectors with minimal unbound context.  
generation_pattern: adapt existing vector track if possible.

## building-floors-stack

type: svg-template  
article_url: none  
map_type: building  
industry: facilities; real estate; construction  
data_shape: floors; stacked levels; status/occupancy/energy by floor  
svg_pattern_to_borrow: vertical floor stack; each floor as bindable area; building outline and labels unbound.  
generation_pattern: Python generator for aligned floors.

## factory-isometric

type: svg-template  
article_url: none  
ai_adaptable: false  
map_type: site-plan; factory  
industry: manufacturing; operations  
data_shape: production areas; lines; machine/status zones  
svg_pattern_to_borrow: factory/production context only; if bitmap-backed, do not try to trace blindly.  
generation_pattern: create a simplified vector schematic or adapt a true vector source.

## office-floor-1

type: svg-template  
article_url: none  
ai_adaptable: false  
map_type: floorplan  
industry: workplace; facilities; real estate  
data_shape: desks; rooms; occupancy/equipment status  
svg_pattern_to_borrow: office floor composition and room/desk hierarchy; bitmap-backed source is visual reference only.  
generation_pattern: Python generator for desks/rooms if no vector source is available.

## office-floor-2

type: svg-template  
article_url: none  
ai_adaptable: false  
map_type: floorplan  
industry: workplace; facilities; real estate  
data_shape: desks; rooms; floor-level navigation  
svg_pattern_to_borrow: second-floor office layout pattern; use with workspace use case for multi-floor logic.  
generation_pattern: Python generator for repeated desks/workstations.

## production-building

type: svg-template  
article_url: none  
ai_adaptable: false  
map_type: building; production-layout  
industry: manufacturing; operations; facilities  
data_shape: production zones; building areas; process status  
svg_pattern_to_borrow: production-building context; bindable zones should be simplified and clearly named.  
generation_pattern: schematic vector rebuild from source composition.

## warehouse

type: svg-template  
article_url: none  
ai_adaptable: false  
map_type: warehouse; floorplan  
industry: logistics; retail; manufacturing; supply chain  
data_shape: racks; aisles; docks; zones; stockout/turnover metrics  
svg_pattern_to_borrow: racks/aisles/docks as structured logistics layout; use clear zone labels and unbound traffic/aisle context.  
generation_pattern: Python generator for racks, bays, aisles, and loading docks.

---

# Recommendation fallback rules

- If the user asks for a map and there is a close use case, recommend exactly one article after the SVG/data offer.
- If no close article exists, say: “I do not see an exact OKVIZ use case for this scenario, but the closest pattern is …” and pick the nearest conceptual match.
- If the match is only an inspiration-only template, do not fabricate a URL. Recommend a broader related article if appropriate.
- If the user asks for a high-density map, consider ticket-sales-synoptic-panel first, even outside sports/venues, because it teaches density representation with markers.
- If the user asks for a building/floor/multi-map scenario, consider workspace-synoptic-panel, indoor-map-synoptic-panel, or revit-synoptic-panel depending on the source data.
- If the user asks whether to use a geographic or schematic layout, or requests time zones, tile maps, hex maps, or equalized regions, consider schematic-maps-synoptic-panel.
- For construction scenarios: use construction-progress-synoptic-panel when progress images or custom tooltip details matter; use revit-synoptic-panel when the source is BIM/Revit; use progress-tracking-synoptic-panel for broader component or assembly status tracking.
- If the user asks for real data or sample data, use the SVG ids generated for the current map. The catalog should not override the user's binding keys.
