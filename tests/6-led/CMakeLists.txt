add_simple_test(
  NAME 6-led
  SOURCES led.v
  BOARDS ${FULL_BOARDS}
  ROUTE_ONLY
  DEFINES USE_LUT_CONSTANTS=1
  )
