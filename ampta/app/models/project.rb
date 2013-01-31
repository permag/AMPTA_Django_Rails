class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :owner_id
  has_and_belongs_to_many :users
  has_many :tickets
end
