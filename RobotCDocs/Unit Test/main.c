


// Here's a nunch of space to test the accruacy of my error logger.












/*
 * Test 1.
 * This line should have a space between this and the last period.
 * This line should also have a space.
 * The function below me should have all of types removed.
*/
void Test1(tMotor motorPort, byte speed, bool reversed);


/*
 * @test
 *
 * Test 2. The function below this should have all pointers removed and be visible.
 * This function should be listed below the "Test" category.
*/
void* Test2(tMotor* motorPort, byte speed, bool* reversed);

/*
 * @test
 *
 * Test 2_2. The function should not be visible at all. There's wayy to many spaces.
*/
void* Test2_2                 (tMotor* motorPort, byte speed, bool* reversed);

/*
 @sensor
 *
 * Test 3. Neither the attribute or the next line should work.
 * This function should be listed in "Main".
 This line should be ignored.
*/
bool test3;

/*
 * @sensor
 * @test
 * This should be under the "Test" category, as it's the most recent.
*/
void test4;

/*
 * @sensor @test
 * This should be under the "Sensor" category, as it's the leftmost attribute.
 * The variable below this should have its pointer removed.
*/
tMotor* test5;


/*
 * This comment should not work.
*/

bool test6Failed.

/*
 * @test7
 * This should be under the "Test7" category.
 *                                   This line should still be visible.
*/
int* test7;


task main() {



}

// Define the functions. This is required.

void Test1(tMotor motorPort, byte speed, bool reversed) {

}

void* Test2(tMotor* motorPort, byte speed, bool* reversed) {

}
