Given(/^I am a citizen$/) do
  #do nothing
end

Given(/^I have logged in$/) do
  #TODO: will need to be addressed as part of US53
end

Given(/^I have a property$/) do
  # empty the database
  delete_all_titles
  # insert the property_hash data into the database
  @property_hash = {
    :title_number => "DN1000",
    :postcode => "PL9 BLT",
    :street_name => "Test Street",
    :house_no => 13,
    :town => "Plymouth",
    :surname => "Marie",
    :forename => "Hill",
    :name_category => "Personal",
    :full_text => "PROPRIETOR: %MARIE HILL% of Flat 113, Eaton Rise, Eton College Road, *London* NW3 2DD.",
    :last_app_timestamp => "2014-01-28T12:38:58+01:00"
  }
  create_proprietor_title_in_db(@property_hash)
end

Given(/^I do not have a property$/) do
  # empty the database
  delete_all_titles
  @property_hash = {
    :title_number => "DN1000"
  }
  #Do not create the title in the database
end

When(/^I view the property detail page$/) do
  visit("http://landregistry.local:8003/titles/#{@property_hash[:title_number]}")
end

Then(/^I see the full address of the property$/) do
  content = page.body.text
  expect(content).to include(@property_hash[:postcode])
  expect(content).to include(@property_hash[:town])
  expect(content).to include("#{@property_hash[:house_no]} #{@property_hash[:street_name]}")
end

Then(/^I see the title number of the property$/) do
  content = page.body.text
  expect(content).to include(@property_hash[:title_number])
end

Then(/^I get a page not found message$/) do
  expect(page.status_code).to eq(404)
end


#*************************************
Given(/^I have a property owned by an individual$/) do
  # empty the database
  delete_all_titles
  # insert the property_hash data into the database
  @property_hash = {
    :title_number => "DN1000",
    :postcode => "NW3 2DD",
    :street_name => "Eaton Rise",
    :house_no => 113,
    :town => "London",
    :surname => "Hill",
    :forename => "Marie",
    :name_category => "Personal",
    :full_text => "PROPRIETOR: %MARIE HILL% of Flat 113, Eaton Rise, Eton College Road, *London* NW3 2DD.",
    :multi_proprietors => "singlePI"
  }
  create_proprietor_title_in_db(@property_hash)
end

Then(/^I can see who owns the property$/) do
  content = page.body.text
  expect(content).to include("#{@property_hash[:forename]} #{@property_hash[:surname]}")
end

Given(/^the property is owned by multiple individuals$/) do
  # empty the database
  delete_all_titles
  # insert the property_hash data into the database
  @property_hash = {
    :title_number => "DN1000",
    :postcode => "NW3 2DD",
    :street_name => "Eaton Rise",
    :house_no => 113,
    :town => "London",
    :surname => "Hicks",
    :forename => "Fred",
    :name_category => "Personal",
    :full_text => "PROPRIETOR: %FRED HICKS% of Flat 113, Eaton Rise, Eton College Road, *London* NW3 2DD.",
    :multi_proprietors => "TwoPI"
  }
  create_proprietor_title_in_db(@property_hash)
end

Then(/^I can see all the owners the property$/) do
  #pending # express the regexp above with the code you wish you had
  content = page.body.text
  expect(content).to include("#{@property_hash[:forename]} #{@property_hash[:surname]}")
  #expect(content).to include("#{@property_hash[:forename2]} #{@property_hash[:surname2]}")
  #expect(content).to include("#{@property_hash[:forename3]} #{@property_hash[:surname3]}")
  #expect(content).to include("#{@property_hash[:forename4]} #{@property_hash[:surname4]}")
end

Then(/^I see the date at which the title was last changed$/) do
  content = page.body.text
  expect(content).to include("28 January 2014 at 12:38:58")
end





#start of sprint three changes dog 24/2
=begin
Given(/^I am an initial private beta user$/) do
  pending # express the regexp above with the code you wish you had
end

Given(/^I have logged in$/) do
  pending # express the regexp above with the code you wish you had
end

Given(/^I have a title with a non private individual owner$/) do
  pending # express the regexp above with the code you wish you had
end

When(/^I view the register details page$/) do
  pending # express the regexp above with the code you wish you had
end

Then(/^I can view the register details for the selected title$/) do
  pending # express the regexp above with the code you wish you had
end

Given(/^I am logged in$/) do
  pending # express the regexp above with the code you wish you had
end

Given(/^I have a title with a charity with trustees that are private individuals$/) do
  pending # express the regexp above with the code you wish you had
end

Then(/^I cannot view the property owner details for the selected title$/) do
  pending # express the regexp above with the code you wish you had
end

Then(/^a message is displayed instead of the property owner details$/) do
  pending # express the regexp above with the code you wish you had
end

Given(/^I have a title with a charity with trustees that are non private individual owners$/) do
  pending # express the regexp above with the code you wish you had
end

Given(/^I have a title with a private individual owner \{this means on SOR\}$/) do
  pending # express the regexp above with the code you wish you had
end

When(/^I view the register detail page$/) do
  pending # express the regexp above with the code you wish you had
end



=end
#end of sprint three changes
